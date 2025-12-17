<script lang="ts">
  import { fade, fly } from 'svelte/transition';
  
  export let data;
  const { projects, future } = data;

  // Define types
  type Project = {
    id?: number;
    name: string;
    project_type: string;
    project_description: string;
  };

  let selectedProject: Project | null = null;
  let selectedIndex: number = 0;
  let isModalOpen: boolean = false;
  let currentCategory: 'projects' | 'future' = 'projects';

  function openModal(project: Project, index: number, category: 'projects' | 'future') {
    selectedProject = project;
    selectedIndex = index;
    currentCategory = category;
    isModalOpen = true;
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    isModalOpen = false;
    selectedProject = null;
    document.body.style.overflow = 'auto';
  }

  function navigateProject(direction: 'next' | 'prev') {
    const items = currentCategory === 'projects' ? projects : future;
    if (direction === 'next' && selectedIndex < items.length - 1) {
      selectedIndex++;
      selectedProject = items[selectedIndex];
    } else if (direction === 'prev' && selectedIndex > 0) {
      selectedIndex--;
      selectedProject = items[selectedIndex];
    }
  }

  function handleKeydown(e: KeyboardEvent) {
    if (!isModalOpen) return;
    if (e.key === 'Escape') closeModal();
    if (e.key === 'ArrowLeft') navigateProject('prev');
    if (e.key === 'ArrowRight') navigateProject('next');
  }

  // Function to split project types by pipe
  function splitProjectTypes(projectType: string): string[] {
    return projectType.split('|').map(type => type.trim()).filter(type => type.length > 0);
  }
</script>

<svelte:window on:keydown={handleKeydown} />

<div class="container mx-auto px-4 py-8 max-w-7xl">
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
    
    <!-- Current Projects Section -->
    <section class="bg-gradient-to-br from-[#393E46]/50 to-[#222831]/50 backdrop-blur-md rounded-3xl p-8 border border-white/10">
      <h1 class="text-4xl font-bold mb-8 text-[#DFD0B8]">Projects</h1>

      {#if projects.length === 0}
        <p class="text-gray-400">No projects found.</p>
      {:else}
        <div class="space-y-3">
          {#each projects as project, index}
            <button
              on:click={() => openModal(project, index, 'projects')}
              class="w-full group text-left cursor-pointer flex items-start gap-3 p-4 rounded-lg hover:bg-white/5 transition-all"
            >
              <span class="text-xl mt-0.5 text-[#DFD0B8] flex-shrink-0">▸</span>
              <div class="flex-1 min-w-0">
                <h3 class="text-lg font-semibold text-gray-200 group-hover:text-[#DFD0B8] transition-colors break-words">
                  {project.name}
                </h3>
              </div>
            </button>
          {/each}
        </div>
      {/if}
    </section>

    <!-- Future Works Section -->
    <section class="bg-gradient-to-br from-[#393E46]/50 to-[#222831]/50 backdrop-blur-md rounded-3xl p-8 border border-white/10">
      <h2 class="text-4xl font-bold mb-8 text-[#DFD0B8]">Future Works</h2>

      {#if future.length === 0}
        <p class="text-gray-400 text-center py-12">More exciting projects coming soon!</p>
      {:else}
        <div class="space-y-3">
          {#each future as work, index}
            <button
              on:click={() => openModal(work, index, 'future')}
              class="w-full group text-left cursor-pointer flex items-start gap-3 p-4 rounded-lg hover:bg-white/5 transition-all"
            >
              <span class="text-xl mt-0.5 text-purple-300 flex-shrink-0">▸</span>
              <div class="flex-1 min-w-0">
                <h3 class="text-lg font-semibold text-gray-200 group-hover:text-purple-300 transition-colors break-words">
                  {work.name}
                </h3>
              </div>
            </button>
          {/each}
        </div>
      {/if}
    </section>

  </div>
</div>

<!-- Modal -->
{#if isModalOpen && selectedProject}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div
    class="fixed inset-0 z-50 flex items-center justify-center p-4"
    transition:fade={{ duration: 200 }}
    on:click={closeModal}
    role="dialog"
    aria-modal="true"
  >
    <!-- Backdrop -->
    <div class="absolute inset-0 bg-black/80 backdrop-blur-sm"></div>

    <!-- Modal Content -->
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div
      class="relative w-full max-w-4xl max-h-[90vh] bg-gradient-to-br from-[#393E46] to-[#222831] rounded-3xl border border-[#DFD0B8]/30 shadow-2xl overflow-hidden"
      transition:fly={{ y: 50, duration: 300 }}
      on:click|stopPropagation
      role="document"
    >
      <!-- Close Button -->
      <button
        on:click={closeModal}
        class="absolute top-6 right-6 z-10 w-10 h-10 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/20 text-white transition-all"
        aria-label="Close modal"
      >
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>

      <!-- Navigation Buttons -->
      {#if selectedIndex > 0}
        <button
          on:click={() => navigateProject('prev')}
          class="absolute left-4 top-1/2 -translate-y-1/2 z-10 w-12 h-12 flex items-center justify-center rounded-full bg-[#DFD0B8]/20 hover:bg-[#DFD0B8]/40 text-[#DFD0B8] transition-all flex-shrink-0"
          aria-label="Previous project"
        >
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
        </button>
      {/if}

      {#if selectedIndex < (currentCategory === 'projects' ? projects : future).length - 1}
        <button
          on:click={() => navigateProject('next')}
          class="absolute right-4 top-1/2 -translate-y-1/2 z-10 w-12 h-12 flex items-center justify-center rounded-full bg-[#DFD0B8]/20 hover:bg-[#DFD0B8]/40 text-[#DFD0B8] transition-all flex-shrink-0"
          aria-label="Next project"
        >
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      {/if}

      <!-- Scrollable Content -->
      <div class="overflow-y-auto max-h-[90vh] px-8 md:px-20 py-8 md:py-12">
        <div class="mb-6">
          <h2 class="text-4xl font-bold text-[#DFD0B8] mb-4 break-words pr-12">{selectedProject.name}</h2>
          
          <!-- Split tags by pipe -->
          <div class="flex flex-wrap gap-2">
            {#each splitProjectTypes(selectedProject.project_type) as tag}
              <span class="inline-block px-4 py-2 text-sm font-semibold bg-[#DFD0B8]/20 text-[#DFD0B8] rounded-full">
                {tag}
              </span>
            {/each}
          </div>
        </div>

        <div class="prose prose-invert max-w-none">
          <p class="text-lg text-gray-200 leading-relaxed mb-8 break-words">
            {selectedProject.project_description}
          </p>
        </div>

        <!-- Navigation Indicator -->
        <div class="mt-12 pt-6 border-t border-white/10">
            <input
            type="range"
            min="0"
            max={(currentCategory === 'projects' ? projects : future).length - 1}
            bind:value={selectedIndex}
            on:input={() => {
              selectedProject = (currentCategory === 'projects' ? projects : future)[selectedIndex];
            }}
            class="w-full h-2 bg-white/10 rounded-full appearance-none cursor-pointer scrollbar-slider"
            />
        </div>
      </div>
    </div>
  </div>
{/if}

<style>
  .container {
    position: relative;
    z-index: 1;
  }

  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .scrollbar-slider::-webkit-slider-thumb {
  appearance: none;
  width: 32px;
  height: 12px;
  border-radius: 10px;
  background: #DFD0B8;
  cursor: pointer;
  transition: all 0.3s ease;
}

.scrollbar-slider::-webkit-slider-thumb:hover {
  background: #F0EAD6;
  transform: scaleY(1.2);
}

.scrollbar-slider::-moz-range-thumb {
  width: 32px;
  height: 12px;
  border-radius: 10px;
  background: #DFD0B8;
  cursor: pointer;
  border: none;
  transition: all 0.3s ease;
}

.scrollbar-slider::-moz-range-thumb:hover {
  background: #F0EAD6;
  transform: scaleY(1.2);
}

/* Mobile Responsiveness */

/* Tablets (768px and below) */
@media (max-width: 768px) {
  /* Reduce modal padding */
  .overflow-y-auto {
    padding: 1.5rem 3rem !important;
  }

  /* Make navigation buttons smaller */
  .absolute.left-4, .absolute.right-4 {
    width: 40px !important;
    height: 40px !important;
  }

  .absolute.left-4 {
    left: 0.5rem !important;
  }

  .absolute.right-4 {
    right: 0.5rem !important;
  }

  /* Reduce title size */
  h2.text-4xl {
    font-size: 2rem !important;
  }

  /* Make close button smaller */
  .absolute.top-6.right-6 {
    top: 1rem !important;
    right: 1rem !important;
    width: 36px !important;
    height: 36px !important;
  }

  /* Adjust tag sizes */
  .inline-block.px-4.py-2 {
    padding: 0.5rem 0.75rem !important;
    font-size: 0.75rem !important;
  }

  /* Reduce description text size */
  .text-lg {
    font-size: 1rem !important;
  }
}

/* Phones (480px and below) */
@media (max-width: 480px) {
  /* Further reduce modal padding */
  .overflow-y-auto {
    padding: 1rem 2.5rem !important;
  }

  /* Hide navigation buttons on small phones, use swipe gestures instead */
  .absolute.left-4, .absolute.right-4 {
    width: 32px !important;
    height: 32px !important;
    opacity: 0.7;
  }

  .absolute.left-4 {
    left: 0.25rem !important;
  }

  .absolute.right-4 {
    right: 0.25rem !important;
  }

  /* Make title smaller */
  h2.text-4xl {
    font-size: 1.5rem !important;
    margin-bottom: 1rem !important;
  }

  /* Make section titles smaller */
  h1.text-4xl, h2.text-4xl {
    font-size: 1.75rem !important;
  }

  /* Smaller close button */
  .absolute.top-6.right-6 {
    top: 0.75rem !important;
    right: 0.75rem !important;
    width: 32px !important;
    height: 32px !important;
  }

  .absolute.top-6.right-6 svg {
    width: 1.25rem !important;
    height: 1.25rem !important;
  }

  /* Smaller navigation arrows */
  .absolute svg {
    width: 1.25rem !important;
    height: 1.25rem !important;
  }

  /* Stack tags vertically on very small screens */
  .flex-wrap {
    gap: 0.5rem !important;
  }

  .inline-block.px-4.py-2 {
    padding: 0.375rem 0.625rem !important;
    font-size: 0.7rem !important;
  }

  /* Reduce description size */
  .text-lg {
    font-size: 0.9rem !important;
    line-height: 1.5 !important;
  }

  /* Make scrollbar slider thinner */
  .scrollbar-slider::-webkit-slider-thumb {
    width: 24px !important;
    height: 10px !important;
  }

  .scrollbar-slider::-moz-range-thumb {
    width: 24px !important;
    height: 10px !important;
  }

  /* Reduce section padding */
  section.bg-gradient-to-br {
    padding: 1.5rem !important;
  }

  /* Make modal take more screen space */
  .max-w-4xl {
    max-width: 95% !important;
  }

  /* Adjust project list items */
  button.w-full.group {
    padding: 0.75rem !important;
  }

  button.w-full.group h3 {
    font-size: 1rem !important;
  }
}

/* Extra small phones (360px and below) */
@media (max-width: 360px) {
  .overflow-y-auto {
    padding: 0.75rem 2rem !important;
  }

  h2.text-4xl {
    font-size: 1.25rem !important;
  }

  .inline-block.px-4.py-2 {
    padding: 0.25rem 0.5rem !important;
    font-size: 0.65rem !important;
  }

  /* Stack everything more compactly */
  .container.mx-auto {
    padding: 1rem !important;
  }
}
</style>