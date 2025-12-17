<script lang="ts">
import { T as Threlte, isInstanceOf } from '@threlte/core';
import { Float, interactivity} from '@threlte/extras';
import * as THREE from 'three';
import gsap from 'gsap';

interactivity();

export let position: [number, number, number] = [0, 0, 0];
export let geometry: THREE.BufferGeometry = new THREE.IcosahedronGeometry(3);
export let rate: number = 0.5;


function getRandomMaterial() {
    console.log('Generated Random Material');
    return new THREE.MeshStandardMaterial(gsap.utils.random([
        { color: "#702963", roughness: 0.5, metalness: 0.8 },
        { color: "cornflowerblue", roughness: 0.2 },
        { color: "#E76F51", roughness: 0.4, metalness: 0.6 },
        { color: "#2A9D8F", roughness: 0.3, metalness: 0.7 }
    ]));
}

function handleClick(event: any) {
    event.object.material = getRandomMaterial();
    gsap.to(event.object.rotation, {
        x: gsap.utils.random(0, 3),
        y: gsap.utils.random(0, 3),
        z: gsap.utils.random(0, 3),
        duration: 1.2,
        ease: "elastic.out(1, 0.3)",
        yoyo: true,
    });
}



const show = true;
</script>

<Threlte.Group position={position.map(p => p * 2) as [number, number, number]}>
    <Float
        speed={5 * rate}
        rotationSpeed={3 * rate}
        rotationIntensity={20 * rate}
        floatIntensity={6 * rate}
    >
        
            <Threlte.Mesh geometry={geometry} interactive onclick={handleClick} material = {getRandomMaterial()}>
            
               
            </Threlte.Mesh>
        
    </Float>
</Threlte.Group>
