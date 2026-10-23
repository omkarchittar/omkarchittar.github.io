const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

const source = fs.readFileSync("assets/js/point-cloud.js", "utf8");
for (const reduced of [false, true]) {
  const points = [];
  const elements = {};
  const listeners = {};
  const context = {
    clearRect() {
      points.length = 0;
    },
    setTransform() {},
    beginPath() {},
    fill() {},
    arc(x, y, radius) {
      assert.ok([x, y, radius].every(Number.isFinite));
      points.push([x, y]);
    },
  };
  for (const id of ["point-cloud", "reconstruction", "cloud-value", "cloud-pause"]) {
    elements[id] = {
      value: "100",
      textContent: "",
      style: {},
      parentElement: { classList: { add() {} } },
      getContext: () => context,
      getBoundingClientRect: () => ({ width: 370, height: 235 }),
      addEventListener(type, listener) {
        listeners[id + ":" + type] = listener;
      },
    };
  }
  let activeFrames = 0;
  let currentColor = "rgb(173, 63, 40)";
  const mutations = [];
  const sandbox = {
    document: { hidden: false, documentElement: {}, getElementById: (id) => elements[id], addEventListener() {} },
    getComputedStyle: () => ({ color: currentColor }),
    matchMedia: () => ({ matches: reduced, addEventListener() {} }),
    devicePixelRatio: 1,
    requestAnimationFrame: () => ++activeFrames,
    cancelAnimationFrame: (id) => {
      if (id) activeFrames--;
    },
    MutationObserver: class {
      constructor(fn) {
        this.fn = fn;
      }
      observe(target, options) {
        mutations.push({ fn: this.fn, options });
      }
    },
    ResizeObserver: class {
      constructor(fn) {
        this.fn = fn;
      }
      observe() {
        this.fn();
      }
    },
    IntersectionObserver: class {
      constructor(fn) {
        this.fn = fn;
      }
      observe() {
        this.fn([{ isIntersecting: true }]);
      }
    },
  };
  vm.runInNewContext(source, sandbox);
  assert.ok(points.length >= 2000, "The reconstructed knot must render");
  assert.equal(activeFrames, reduced ? 0 : 1, "Respect the motion preference");
  const fullShape = JSON.stringify(points);
  elements.reconstruction.value = "0";
  listeners["reconstruction:input"]();
  assert.equal(elements["cloud-value"].value, "0%");
  assert.notEqual(JSON.stringify(points), fullShape, "Slider must change the geometry");
  elements.reconstruction.value = "100";
  listeners["reconstruction:input"]();
  assert.equal(JSON.stringify(points), fullShape, "Reconstruction must be deterministic");
  if (!reduced) {
    listeners["cloud-pause:click"]();
    assert.equal(activeFrames, 0, "Pause must stop animation");
    assert.equal(elements["cloud-pause"].textContent, "Resume motion");
  }
  currentColor = "rgb(210, 130, 100)";
  for (const observer of mutations) if (observer.options.attributeFilter.includes("data-theme")) observer.fn();
  currentColor = "rgb(242, 160, 131)";
  for (const observer of mutations) if (observer.options.attributeFilter.includes("class")) observer.fn();
  assert.equal(context.fillStyle, currentColor, "Paused cloud must redraw after theme transitions finish");
}
console.log("Point cloud: geometry, reconstruction, reduced motion and pause checks passed.");
