(() => {
  "use strict";
  const canvas = document.getElementById("point-cloud");
  const slider = document.getElementById("reconstruction");
  const output = document.getElementById("cloud-value");
  if (!canvas || !slider || !output) return;
  const context = canvas.getContext("2d");
  if (!context) return;
  const pauseButton = document.getElementById("cloud-pause");
  canvas.parentElement.classList.add("cloud-ready");

  // Procedural artwork, rather than sensor data or a representation of a project.
  const columns = 120;
  const samples = Array.from({ length: columns * 18 }, (_, index) => {
    const u = ((index % columns) / columns) * Math.PI * 2;
    const v = (Math.floor(index / columns) / 18) * Math.PI * 2;
    const center = [(Math.sin(u) + 2 * Math.sin(2 * u)) * 0.4, (Math.cos(u) - 2 * Math.cos(2 * u)) * 0.4, -Math.sin(3 * u) * 0.4];
    const derivative = [Math.cos(u) + 4 * Math.cos(2 * u), -Math.sin(u) + 4 * Math.sin(2 * u), -3 * Math.cos(3 * u)];
    const length = Math.hypot(...derivative);
    const tangent = derivative.map((value) => value / length);
    const sideLength = Math.hypot(tangent[0], tangent[1]);
    const normal = [-tangent[1] / sideLength, tangent[0] / sideLength, 0];
    const binormal = [-tangent[2] * normal[1], tangent[2] * normal[0], tangent[0] * normal[1] - tangent[1] * normal[0]];
    const target = center.map((value, axis) => value + 0.18 * (Math.cos(v) * normal[axis] + Math.sin(v) * binormal[axis]));
    const scatter = [Math.sin(index * 19.13), Math.sin(index * 7.71), Math.cos(index * 13.17)].map((value) => value * 1.8);
    return { target, scatter };
  });

  function pointAt(index, amount) {
    const { target, scatter } = samples[index];
    return target.map((value, axis) => scatter[axis] + (value - scatter[axis]) * amount);
  }

  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
  let paused = reducedMotion.matches;
  const visibility = new IntersectionObserver((entries) => {
    onScreen = entries[0].isIntersecting;
    syncAnimation();
  });
  let onScreen = false;
  let frame = 0;
  let angle = 0.6;
  let lastTime = 0;
  let width = 700;
  let height = 580;

  function draw() {
    const amount = Number(slider.value) / 100;
    const color = getComputedStyle(canvas).color;
    const scale = Math.min(width, height) * 0.23;
    const cos = Math.cos(angle);
    const sin = Math.sin(angle);
    context.clearRect(0, 0, width, height);
    const points = [];
    for (let i = 0; i < samples.length; i++) {
      const [x, y, z] = pointAt(i, amount);
      const rx = x * cos - z * sin;
      const rz = x * sin + z * cos;
      const ry = y * 0.77 - rz * 0.64;
      const depth = y * 0.64 + rz * 0.77;
      points.push({ x: width / 2 + rx * scale, y: height / 2 + ry * scale, depth });
    }
    points.sort((a, b) => a.depth - b.depth);
    for (const point of points) {
      const opacity = Math.max(0.14, Math.min(0.95, (point.depth + 2.6) / 5));
      const radius = 0.7 + opacity * 1.1;
      context.fillStyle = color;
      context.globalAlpha = opacity;
      context.beginPath();
      context.arc(point.x, point.y, radius, 0, Math.PI * 2);
      context.fill();
    }
  }

  function animate(time) {
    if (lastTime) angle += Math.min(time - lastTime, 50) * 0.00012;
    lastTime = time;
    draw();
    frame = requestAnimationFrame(animate);
  }

  function syncAnimation() {
    cancelAnimationFrame(frame);
    frame = 0;
    lastTime = 0;
    pauseButton.textContent = paused ? "Resume motion" : "Pause motion";
    if (!paused && onScreen && !document.hidden) frame = requestAnimationFrame(animate);
    else draw();
  }

  function resize() {
    const rect = canvas.getBoundingClientRect();
    width = rect.width;
    height = rect.height;
    const ratio = Math.min(devicePixelRatio || 1, 2);
    canvas.width = Math.round(width * ratio);
    canvas.height = Math.round(height * ratio);
    context.setTransform(ratio, 0, 0, ratio, 0, 0);
    draw();
  }

  slider.addEventListener("input", () => {
    output.value = `${slider.value}%`;
    draw();
  });
  pauseButton.addEventListener("click", () => {
    paused = !paused;
    syncAnimation();
  });
  reducedMotion.addEventListener("change", (event) => {
    paused = event.matches;
    syncAnimation();
  });
  document.addEventListener("visibilitychange", syncAnimation);
  new MutationObserver(draw).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme", "class"] });
  new ResizeObserver(resize).observe(canvas);
  visibility.observe(canvas);
  resize();
})();
