// === HUMAN–MATRIX 3D GRID ===
let scene, camera, renderer, cubes = [];

function initMatrixGrid() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    camera.position.z = 15;

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('matrix-grid-container').appendChild(renderer.domElement);

    const gridSize = 6;
    const spacing = 2;
    const cubeGeometry = new THREE.BoxGeometry(1, 1, 1);

    for(let x = -gridSize; x <= gridSize; x++) {
        for(let y = -gridSize; y <= gridSize; y++) {
            const cubeMaterial = new THREE.MeshStandardMaterial({
                color: 0x00ffcc,
                roughness: 0.6,
                metalness: 0.3
            });
            const cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
            cube.position.set(x*spacing, y*spacing, 0);
            scene.add(cube);
            cubes.push(cube);
        }
    }

    // Lights
    const ambient = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambient);
    const directional = new THREE.DirectionalLight(0xffffff, 0.8);
    directional.position.set(5,10,7);
    scene.add(directional);

    animate();
}

function animate() {
    requestAnimationFrame(animate);
    const time = Date.now() * 0.001;

    // Animate cubes (simulate matrix pulses)
    cubes.forEach((cube,i)=>{
        cube.rotation.x = time + i*0.01;
        cube.rotation.y = time + i*0.02;
        cube.position.z = Math.sin(time + i*0.3);
        cube.material.color.setHSL(Math.sin(time + i*0.1)*0.5 + 0.5, 0.7, 0.5);
    });

    renderer.render(scene, camera);
}

// Initialize grid after DOM loaded
window.addEventListener('DOMContentLoaded', initMatrixGrid);
