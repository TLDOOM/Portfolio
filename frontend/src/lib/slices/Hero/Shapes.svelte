<script lang="ts">
  import { T } from '@threlte/core';
  import Geometry from "./Geometry.svelte";
  import * as THREE from 'three';
  import { ContactShadows, Environment } from '@threlte/extras';
</script>

<T.PerspectiveCamera makeDefault position={[0,0,25]} fov={30} near={1} far={40} />
<Environment url="/smallroom.hdr" />
<ContactShadows position={[0,-3.5,0]} opacity={0.65} scale={40} blur={1} far={9} />

<Geometry position={[0, 0, 0]} rate={0.4} geometry={new THREE.SphereGeometry(2.5, 100, 16)} />
<Geometry position={[0, 1.1, 3]} rate={1} geometry={new THREE.CapsuleGeometry(0.3, 1, 3, 20)} />
<Geometry position={[0.8, -0.8, 2]} rate={0.7} geometry={new THREE.DodecahedronGeometry(0.75)} />
<Geometry position={[1, 0.8, 2]} rate={0.7} geometry={new THREE.TorusGeometry(1, 0.3, 20, 60)} />
<Geometry position={[-1.3, -1.2, -3]} rate={0.7} geometry={new THREE.IcosahedronGeometry(1)} />
<Geometry position={[-1.3, 1.3, -2]} rate={0.7} geometry={new THREE.OctahedronGeometry(1)} />
