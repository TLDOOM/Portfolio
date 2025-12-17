import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	ssr: {
		noExternal: ['three']
	},
	
	plugins: [tailwindcss(), sveltekit()],
	server: {
		fs: {
			allow: ['./slicemachine.config.json']
		}
	}
});
