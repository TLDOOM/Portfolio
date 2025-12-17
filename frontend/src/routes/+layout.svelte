<script>
	import { page } from '$app/stores';
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';
	import mylogo from '$lib/assets/my_logo.png';
	import "../app.css";
	import "@fontsource-variable/manrope";
	

	let headerVisible = true;
	let lastScroll = 0;
	let isMenuOpen = false;

	onMount(() => {
		const handleScroll = () => {
			const currentScroll = window.pageYOffset;
			
			if (currentScroll <= 0) {
				headerVisible = true;
				return;
			}
			
			if (currentScroll > lastScroll && currentScroll > 100) {
				// Scrolling down & past 100px
				headerVisible = false;
				isMenuOpen = false; // Close menu when hiding header
			} else if (currentScroll < lastScroll) {
				// Scrolling up
				headerVisible = true;
			}
			
			lastScroll = currentScroll;
		};

		window.addEventListener('scroll', handleScroll);
		
		return () => {
			window.removeEventListener('scroll', handleScroll);
		};
	});

	function toggleMenu() {
		isMenuOpen = !isMenuOpen;
	}

	function closeMenu() {
		isMenuOpen = false;
	}
</script>

<style>
	/* BODY BACKGROUND */
	:global(body) {
		background: linear-gradient(to bottom right, oklch(55.2% 0.016 285.938), oklch(44.2% 0.017 285.786), oklch(26.9% 0 0));
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		margin: 0;
		padding: 0;
		 font-family: 'Manrope Variable', sans-serif;
	}

	:global(body)::before {
		content: '';
		position: fixed;
		inset: 0;
		background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
		opacity: 0.15;
		pointer-events: none;
		z-index: 0;
	}

	/* HEADER */
	header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 1.5rem 3rem;
		background: rgba(148, 137, 121, 0.3);
		backdrop-filter: blur(30px);
		position: fixed;
		top: 0.75rem;
		left: 50%;
		transform: translateX(-50%);
		z-index: 10;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
		max-width: 1400px	;
		width: calc(100% - 2rem);
		border-radius: 16px;
		gap: 15rem;
		border: 1px solid rgba(255, 255, 255, 0.1);
		transition: transform 0.3s ease-in-out;
	}

	header.hidden {
		transform: translateX(-50%) translateY(-120%);
	}

	.logo {
		width: 50%;
  		height: auto;
		max-width: 40px;
	}

	/* Desktop Navigation */
	nav {
		display: flex;
		gap: 2rem;
	}

	nav a {
		color: #e9fff5;
		text-decoration: none;
		font-weight: 500;
		padding: 0.4rem 0.7rem;
		border-radius: 6px;
		transition: all 0.25s ease;
	}

	nav a:hover {
		background: #DFD0B8;
	}

	nav a.active {
		background: #393E46;
		color: #DFD0B8;
		font-weight: 600;
		box-shadow: 0 3px 10px rgba(0, 0, 0, 0.25);
	}

	/* Hamburger Button */
	.hamburger-btn {
		display: none;
		background: none;
		border: none;
		cursor: pointer;
		padding: 0.5rem;
		color: #e9fff5;
		z-index: 20;
	}

	.hamburger-btn svg {
		width: 28px;
		height: 28px;
	}

	/* Mobile Navigation */
	.mobile-nav {
		display: none;
		position: fixed;
		top: 5rem;
		left: 50%;
		transform: translateX(-50%);
		width: calc(100% - 2rem);
		max-width: 800px;
		background: rgba(148, 137, 121, 0.95);
		backdrop-filter: blur(30px);
		border-radius: 16px;
		border: 1px solid rgba(255, 255, 255, 0.1);
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
		padding: 1rem;
		z-index: 9;
	}

	.mobile-nav.open {
		display: block;
	}

	.mobile-nav a {
		display: block;
		color: #e9fff5;
		text-decoration: none;
		font-weight: 500;
		padding: 0.75rem 1rem;
		border-radius: 8px;
		transition: all 0.25s ease;
		margin-bottom: 0.5rem;
	}

	.mobile-nav a:hover {
		background: rgba(223, 208, 184, 0.3);
	}

	.mobile-nav a.active {
		background: #393E46;
		color: #DFD0B8;
		font-weight: 600;
	}

	/* RESPONSIVE BREAKPOINTS */
	@media (max-width: 768px) {
		header {
			padding: 1rem 1.5rem;
			gap: 0;
		}

		nav {
			display: none;
		}

		.hamburger-btn {
			display: block;
		}
	}

	/* MAIN WRAPPER */
	main {
		flex: 1;
		position: relative;
		z-index: 1;
		width: 100%;
		padding-top: 6rem;
	}

	.page {
		width: 100%;
	}

	/* FOOTER */
	footer {
		background: rgba(0, 0, 0, 0.15);
		backdrop-filter: blur(10px);
		padding: 0.5rem;
		text-align: center;
		color: #c8f9e0;
		font-size: 0.9rem;
		margin-top: 2rem;
		border-top: 1px solid rgba(255, 255, 255, 0.15);
		position: relative;
		z-index: 1;
	}

</style>

<header class:hidden={!headerVisible}>
	<div class="logo"><a href="/" class={$page.url.pathname === "/" ? "active" : ""}><img src = {mylogo}/></a></div>

	<!-- Desktop Navigation -->
	<nav>
		<a href="/" class={$page.url.pathname === "/" ? "active" : ""}>Home</a>
		<a href="/about" class={$page.url.pathname === "/about" ? "active" : ""}>About Me</a>
		<a href="/projects" class={$page.url.pathname === "/projects" ? "active" : ""}>Projects</a>
	</nav>

	<!-- Hamburger Button (Mobile Only) -->
	<button class="hamburger-btn" on:click={toggleMenu} aria-label="Toggle menu">
		{#if !isMenuOpen}
			<svg fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
			</svg>
		{:else}
			<svg fill="none" viewBox="0 0 24 24" stroke="currentColor">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
			</svg>
		{/if}
	</button>
</header>

<!-- Mobile Navigation Menu -->
<div class="mobile-nav" class:open={isMenuOpen}>
	<a href="/" class={$page.url.pathname === "/" ? "active" : ""} on:click={closeMenu}>Home</a>
	<a href="/about" class={$page.url.pathname === "/about" ? "active" : ""} on:click={closeMenu}>About Me</a>
	<a href="/projects" class={$page.url.pathname === "/projects" ? "active" : ""} on:click={closeMenu}>Projects</a>
</div>

<main>
	{#key $page.url.pathname}
		<div class="page" in:fade={{ duration: 400, delay: 400 }}>
			<slot />
		</div>
	{/key}
</main>

<footer>

	<div>
		© {new Date().getFullYear()} Tracy Lansang — All Rights Reserved
	</div>
</footer>