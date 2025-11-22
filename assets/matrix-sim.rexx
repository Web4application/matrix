// === HUMAN–MATRIX XLSL SIMULATION ===

const state = {
    ΔH: 1.0,     // cellular energy
    Ψ⚡: 1.0,     // neural signal
    ♥︎: 1.0,     // heart EM
    IR: 1.0,     // body IR
    EM: 1.0,     // external EM field
    g: 1.0,      // gravity alignment
    entropy: 0.1,
    brainLoad: 0,
    realityRendered: false
};

// Formula: Reality_Rendered = Ω~(ꜱΠ(...))
function computeReality() {
    const humanSignal =
        state.ΔH +
        state.Ψ⚡ +
        state.♥︎ +
        state.IR;

    const matrixField = state.EM * state.g;

    const combined = humanSignal * matrixField * (1 - state.entropy);

    state.realityRendered = combined > 2.5;

    document.querySelector("#reality-status").innerHTML =
        state.realityRendered ? "✔ Matrix Decoding Active" : "… Weak Signal";
}

// Brain collapse
function updateBrain() {
    state.brainLoad += state.entropy * 0.05;

    if (state.brainLoad > 1.0) {
        document.querySelector("#brain-status").innerHTML =
            "⚠ Brain Collapse";
    } else {
        document.querySelector("#brain-status").innerHTML =
            "Stable";
    }
}

// Run simulation
setInterval(() => {
    computeReality();
    updateBrain();
}, 300);
