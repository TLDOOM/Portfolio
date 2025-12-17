<script lang="ts">
	import {Canvas} from "@threlte/core"
	import Shapes from "./Shapes.svelte"
	import Scene from './Scene.svelte';
</script>

<section class="px-4 md:px-6 overflow-hidden">
	<div class="py-8">
		<div class="grid min-h-[65vh] grid-cols-1 items-center gap-8 lg:gap-72 lg:grid-cols-2 px-4 md:px-12">
			
			<!-- 3D SCENE (First on mobile/tablet, Second on desktop) -->
			<div class="relative h-[40vh] md:h-[50vh] lg:h-[80vh] flex items-center justify-center scale-100 md:scale-110 lg:scale-125 xl:scale-150 order-1 lg:order-2">
				<div class="w-full h-full">
					<Scene />
				</div>
			</div>

			<!-- TEXT (Second on mobile/tablet, First on desktop) -->
			<div class="flex flex-col justify-center order-2 lg:order-1">
				<h1 class="mb-2 md:mb-6 lg:mb-8 text-[clamp(2.5rem,8vmin,13rem)] lg:text-[clamp(8rem,8vmin,13rem)] font-extrabold leading-none tracking-tight	">
					<span class="block text-[#DFD0B8] -mt-[0.8em]">Tracy</span>
					
					<span class="block text-[#222831] -mt-[.1em]">Lansang</span>
				</h1>

				<span class="block bg-gradient-to-tr from-zinc-500 via-zinc-300 to-zinc-500 bg-clip-text text-transparent text-xl md:text-2xl lg:text-3xl font-bold uppercase tracking-[.2em]">
					Software Engineer
				</span>
			</div>

		</div>
	</div>
</section>