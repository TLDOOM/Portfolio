<script>
import gitlogo from '$lib/assets/github.png';
import linklogo from '$lib/assets/linkedin.png';
import me from '$lib/assets/me.jpg';
import tech_1 from '$lib/assets/FastAPI.svg';
import tech_2 from '$lib/assets/docker.svg';
import tech_3 from '$lib/assets/SvelteLogo.png';
import tech_4 from '$lib/assets/sqlite-icon.svg';
import tech_5 from '$lib/assets/Logo_C_sharp.svg';
import py_Cert from '$lib/assets/Py_Cert.jpg';
import pmi_Cert from '$lib/assets/PMI_Cert.jpg';
import { fly,fade } from 'svelte/transition';
import CCNA from '$lib/assets/CCNA.jpg';
import Devnet from '$lib/assets/Devnet.jpg';
import JuniorCyber from '$lib/assets/JuniorCyber.jpg';
import hidden from '$lib/assets/hidden.jpg';

let selectedTech = null;
let showCertGallery = false;
let currentCertIndex = 0;
let showEmailModal = false;
let emailForm = {
    subject: '',
    body: '',
    from_name: '',
    from_email: ''
};
let sending = false;
let emailStatus = '';
let touchStartX = 0;
let touchEndX = 0;

const certifications = [
    { name: "Cisco DevNet Associate", image: Devnet },
    { name: "Python Certification", image: py_Cert },
    { name: "Cisco CCNA", image: CCNA },
    { name: "PMI Certification", image: pmi_Cert },
    { name: "CompTIA Junior Cybersecurity Analyst", image: JuniorCyber }
];

const techStack = [
    { 
        id: 1, 
        name: "FastAPI", 
        icon: tech_1, 
        description: "FastAPI is my primary backend framework, chosen for its performance and seamless integration with other frameworks and machine learning models.      Its asynchronous capabilities allow me to build scalable applications efficiently \n\n\n (This website uses fastAPI :D)."
    },
    { 
        id: 2, 
        name: "Docker", 
        icon: tech_2, 
        description: "I use Docker to containerize applications, ensuring consistent environments across development and production. This streamlines deployment and enhances scalability for my projects."
    },
    { 
        id: 3, 
        name: "Svelte", 
        icon: tech_3, 
        description: "I just started using Svelte for frontend development due to its simplicity and performance. Its reactive nature allows me to build dynamic user interfaces with less boilerplate code."
    },
    { 
        id: 4, 
        name: "SQLite", 
        icon: tech_4, 
        description: "I use SQLite for lightweight database management in my projects. Its serverless architecture makes it easy to set up and maintain, ideal for small to medium-sized applications."
    },
    { 
        id: 5, 
        name: "C#", 
        icon: tech_5, 
        description: "C# is a versatile programming language I use for developing a variety of applications, I began learning on it through Unity for game development and have since expanded to building desktop and game modding with .NET."
    }
];

function openTechModal(tech) {
    selectedTech = tech;
}

function closeTechModal() {
    selectedTech = null;
}

function openCertGallery() {
    showCertGallery = true;
    currentCertIndex = 0;
}

function closeCertGallery() {
    showCertGallery = false;
}

function nextCert() {
    currentCertIndex = (currentCertIndex + 1) % certifications.length;
}

function prevCert() {
    currentCertIndex = (currentCertIndex - 1 + certifications.length) % certifications.length;
}

function handleTouchStart(e) {
    touchStartX = e.changedTouches[0].screenX;
}

function handleTouchEnd(e) {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
}

function handleSwipe() {
    const swipeThreshold = 50; // Minimum pixels moved to count as a swipe
    if (touchEndX < touchStartX - swipeThreshold) {
        nextCert(); // Swiped left
    }
    if (touchEndX > touchStartX + swipeThreshold) {
        prevCert(); // Swiped right
    }
}

function openEmailModal() {
    showEmailModal = true;
    emailForm = {
        subject: '',
        body: '',
        from_name: '',
        from_email: ''
    };
    emailStatus = '';
}

function closeEmailModal() {
    showEmailModal = false;
    sending = false;
    emailStatus = '';
}

async function sendEmail() {
    if (!emailForm.subject || !emailForm.body || !emailForm.from_name || !emailForm.from_email) {
        emailStatus = 'Please fill in all fields';
        return;
    }

    sending = true;
    emailStatus = '';

    try {
        const result = await emailjs.send(
            'service_yvsuifr',
            'template_e5jdg78',
            {
                from_name: emailForm.from_name,
                from_email: emailForm.from_email,
                subject: emailForm.subject,
                message: emailForm.body,
                to_email: 'tjlansang123@gmail.com'
            }
        );
        
        emailStatus = 'Email sent successfully!';
        setTimeout(() => {
            closeEmailModal();
        }, 2000);
    } catch (error) {
        emailStatus = 'Failed to send email. Please try again.';
        console.error('EmailJS error:', error);
    } finally {
        sending = false;
    }
}

let showHidden = false
  let hoverTimeout

  function handleMouseEnter() {
    hoverTimeout = setTimeout(() => {
      showHidden = true
    }, 5000)
  }

  function handleMouseLeave() {
    clearTimeout(hoverTimeout)
    showHidden = false
  }
</script>

<style>


.page {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.about-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
    min-height: 70vh;
    padding: 4rem 6rem;
    max-width: 1400px;
    margin: 0 auto;
    width: 100%;
}

.about-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.about-content h1 {
    font-size: clamp(3rem, 8vw, 5rem);
    font-weight: 800;
    margin-bottom: 2rem;
    text-shadow: 0px 6px 12px rgba(0, 0, 0, 0.4);
    color:#222831;
    letter-spacing: -0.02em;
}

@keyframes gradientText {
    0%,100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.about-content p {
    font-size: clamp(1.125rem, 2vw, 1.5rem);
    line-height: 1.7;
    color: #F0EAD6;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.profile-image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    
}

.profile-image {
    width: 100%;
    max-width: 400px;
    height: 400px;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    object-fit: cover;
}

.hidden-image {
   width: 100%;
    max-width: 400px;
    height: 400px;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    object-fit: cover;
    opacity: 1;
  transition: opacity 0.3s ease;
}

.hidden {
  opacity: 0;
}

.tech-stack-section {
    background: rgba(255, 255, 255, 0.05);
    padding: 3rem 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.tech-stack-title {
    text-align: center;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 2rem;
    color: #222831;
}

.tech-stack-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6.5rem;
    flex-wrap: wrap;
    max-width: 1200px;
    margin: 0 auto;
}

.tech-logo {
    width: 80px;
    height: 80px;
    object-fit: contain;
    transition: transform 0.3s ease, opacity 0.3s ease;
    filter: grayscale(20%);
    cursor: pointer;
}

.tech-logo:hover {
    transform: scale(1.1);
    opacity: 0.8;
    filter: grayscale(20%);
}

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(5px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    animation: fadeIn 0.2s ease;
    white-space: pre-line;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.modal-content {
    background: rgba(30, 30, 40, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    padding: 2rem;
    max-width: 500px;
    width: 90%;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    position: relative;
    animation: slideUp 0.3s ease;
}

@keyframes slideUp {
    from { 
        transform: translateY(30px);
        opacity: 0;
    }
    to { 
        transform: translateY(0);
        opacity: 1;
    }
}

.modal-header {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.modal-icon {
    width: 60px;
    height: 60px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    font-weight: bold;
    flex-shrink: 0;
}

.modal-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: rgba(255, 255, 255, 0.95);
    margin: 0;
}

.modal-description {
    font-size: 1.1rem;
    line-height: 1.7;
    color: rgba(255, 255, 255, 0.85);
    margin: 0;
}

.modal-close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: rgba(255, 255, 255, 0.1);
    border: none;
    color: rgba(255, 255, 255, 0.9);
    font-size: 1.5rem;
    width: 36px;
    height: 36px;
    border-radius: 8px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s ease;
}

.modal-close:hover {
    background: rgba(255, 255, 255, 0.2);
}

.sub-sections {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 3rem;
    padding: 4rem 6rem;
    max-width: 1400px;
    margin: 0 auto;
    width: 100%;
}

.sub-section {
    background: rgba(255, 255, 255, 0.03);
    border-radius: 16px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.sub-section:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.sub-section h2 {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    color: #222831;
}

.interests-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.interests-list li {
    font-size: 1.2rem;
    line-height: 2;
    color: #DFD0B8;
    padding-left: 1.5rem;
    position: relative;
}

.interests-list li:before {
    content: "▹";
    position: absolute;
    left: 0;
    color: oklch(70.4% 0.04 256.788);
}

.cert-box {
    cursor: pointer;
    transition: background 0.3s ease;
}

.cert-box:hover {
    background: rgba(255, 255, 255, 0.05);
}

.cert-thumbnail {
    width: 100%;
    max-width: 250px;
    height: auto;
    border-radius: 12px;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-top: 1rem;
}

.cert-thumbnail:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

.gallery-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.9);
    backdrop-filter: blur(10px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2000;
    animation: fadeIn 0.3s ease;
}

.gallery-content {
    position: relative;
    max-width: 90%;
    max-height: 90%;
    display: flex;
    align-items: center;
    gap: 2rem;
}

.gallery-image {
    max-width: 800px;
    max-height: 80vh;
    width: auto;
    height: auto;
    border-radius: 12px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    animation: slideUp 0.3s ease;
}

.gallery-nav {
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: white;
    font-size: 2rem;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    justify-content: center;
    transition: background 0.2s ease;
    align-items: center;
    line-height: 50px;
}

.gallery-nav-icon{
    transform: translateY(-5px);
}

.gallery-nav:hover {
    background: rgba(255, 255, 255, 0.2);
}

.gallery-close {
    position: absolute;
    top: -50px;
    right: 0;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: white;
    font-size: 1.5rem;
    width: 40px;
    height: 40px;
    border-radius: 8px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s ease;
}

.gallery-close:hover {
    background: rgba(255, 255, 255, 0.2);
}

.gallery-counter {
    position: absolute;
    bottom: -40px;
    left: 50%;
    transform: translateX(-50%);
    color: rgba(255, 255, 255, 0.9);
    font-size: 1rem;
}

.contact-section {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02));
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding: 4rem 2rem;
    margin-top: 2rem;
}

.contact-container {
    max-width: 1000px;
    margin: 0 auto;
    text-align: center;
}

.contact-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    background: linear-gradient(0deg,#393E46,#222831);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.contact-subtitle {
    font-size: 1.2rem;
    color: #DFD0B8;
    margin-bottom: 2rem;
}

.contact-info {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 3rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}

.contact-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
}

.contact-label {
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.6);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.contact-value {
    font-size: 1.2rem;
    color: #DFD0B8;
}

.contact-value a {
   color: #DFD0B8;
    text-decoration: none;
 
}


.social-logos {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    margin-top: 4rem;
}

.social-logo {
    width: 50px;
    height: 50px;
    transition: transform 0.3s ease, opacity 0.3s ease;
}

.social-logo:hover {
    transform: scale(1.1);
    opacity: 0.7;
}

.email-button {
    background: linear-gradient(135deg,#393E46,#393E46);
    color: white;
    border: none;
    padding: 1rem 1.5rem;
    font-size: 1.1rem;
    font-weight: 600;
    border-radius: 50px;
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    margin-bottom: 3rem;
}

.email-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.container-box {
  /* 1. Firefox Support */
  scrollbar-width: thin;
  scrollbar-color: #2d2d2d #2d2d2d; /* thumb color | track color */

  /* 2. Chrome, Edge, and Safari Support */
  max-height: 500px;
  overflow-y: auto;
}

.email-modal-content::-webkit-scrollbar {
  width: 8px; 
}

.email-modal-content::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 10px;
}

.email-modal-content::-webkit-scrollbar-thumb:hover{
    background: rgba(255, 255,255, 0.4);
  
}

.email-modal-content::-webkit-scrollbar-track {
  background: transparent; 
  margin:8px 0;
  border-radius: 10px;
}

.email-modal-content {
    background: rgba(30, 30, 40, 0.98);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    padding: 2.5rem;
    max-width: 550px;
    width: 90%;
    height: auto;
    max-height: 83vh;
    overflow-y: auto;
   
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    position: relative;
    animation: slideUp 0.3s ease;
    margin:20px auto;
}

.email-modal-title {
    font-size: 2rem;
    font-weight: 700;
    color: rgba(255, 255, 255, 0.95);
    margin-bottom: 1.5rem;
    text-align: center;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-label {
    display: block;
    font-size: 1rem;
    color: rgba(255, 255, 255, 0.9);
    margin-bottom: 0.5rem;
    font-weight: 500;
}

.form-input,
.form-textarea {
    width: 100%;
    padding: 0.75rem 1rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    color: rgba(255, 255, 255, 0.9);
    font-size: 1rem;
    transition: border-color 0.3s ease, background 0.3s ease;
}

.form-input:focus,
.form-textarea:focus {
    outline: none;
    border-color: oklch(70.4% 0.04 256.788);
    background: rgba(255, 255, 255, 0.08);
}

.form-textarea {
    min-height: 150px;
    resize: vertical;
    font-family: inherit;
}

.form-buttons {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
}

.send-button,
.cancel-button {
    flex: 1;
    padding: 0.875rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
}

.send-button {
    background: linear-gradient(135deg, oklch(70.4% 0.04 256.788), oklch(55.4% 0.046 257.417));
    color: white;
}

.send-button:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.send-button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.cancel-button {
    background: rgba(255, 255, 255, 0.1);
    color: rgba(255, 255, 255, 0.9);
}

.cancel-button:hover {
    background: rgba(255, 255, 255, 0.15);
}

.email-status {
    margin-top: 1rem;
    padding: 0.75rem;
    border-radius: 8px;
    text-align: center;
    font-size: 0.95rem;
}

.email-status.success {
    background: rgba(34, 197, 94, 0.2);
    color: #4ade80;
    border: 1px solid rgba(34, 197, 94, 0.3);
}

.email-status.error {
    background: rgba(239, 68, 68, 0.2);
    color: #f87171;
    border: 1px solid rgba(239, 68, 68, 0.3);
}

p {
    color: #DFD0B8;
}

@media (max-width: 968px) {
    
    
    .about-section {
        grid-template-columns: 1fr;
        padding: 3rem 2rem;
        gap: 2rem;
    }

    .sub-sections {
        grid-template-columns: 1fr;
        padding: 1.5rem 2rem;
        gap: 2rem;
    }

    .tech-stack-container {
        gap: 2rem;
    }

    .tech-logo {
        width: 60px;
        height: 60px;
    }

    .tech-logo:hover {
    transform: scale(1.1);
    opacity: 0.8;
    filter: grayscale(20%);
}

    .contact-info {
        flex-direction: column;
        gap: 1.5rem;
    }

    .gallery-content {
        width: 95%;
        height: auto;
        max-height: 80vh;
        display: flex;
        flex-direction: column; /* Stack image and controls vertically if needed */
        position: relative;
       
    }

    .gallery-image {
        width: 100%;
        max-height: 60vh; /* Keeps the image from pushing the counter off-screen */
        object-fit: contain;
    }

    /* Make nav buttons larger for thumbs */
    .gallery-nav {
        width: 50px;
        height: 50px;
        font-size: 2rem;
        background: rgba(0, 0, 0, 0.5);
        text-align: center; /* Semi-transparent for visibility */
        position: relative;
        offset: 30px;
        visibility: hidden;
       
    }

    /* Position nav buttons so they don't cover the center of the image */
    .gallery-nav:first-of-type { left: 10px; }
    .gallery-nav:last-of-type { right: 10px; }

    .gallery-counter {
        margin-top: 1rem;
        font-size: 0.9rem;
    }
}
@media(max-width:1024px){
    .gallery-nav{
        visibility: hidden;
    }
}
</style>

<div class="page">
    <section class="about-section">
        <div class="about-content">
            <h1>Who am I?</h1>
            <p>
                I am Tracy Lansang, an aspiring software engineer. My goal in life is to learn and
                accumulate experience as much as possible, as the end goal of my journey is to be
                able to teach Computer Science at a university level.
            </p>
        </div>
        <div class="profile-image-container"
            on:mouseenter={handleMouseEnter}
             on:mouseleave={handleMouseLeave}>
             
            <div style="width: 100%; max-width: 400px; height: 400px; background: linear-gradient(135deg, oklch(70.4% 0.04 256.788), oklch(37.2% 0.044 257.287)); border-radius: 20px; display: flex; align-items: center; justify-content: center;">
                <img src={me} alt="Tracy Lansang" class="profile-image" class:hidden={showHidden}/>
                <img
                src={hidden}
                 class:hidden={!showHidden}
                    class="hidden-image"
                    />
            </div>
        </div>
    </section>

    <section class="tech-stack-section">
        <h2 class="tech-stack-title">Tech Stack</h2>
        <div class="tech-stack-container">
            {#each techStack as tech}
                <!-- svelte-ignore a11y_no_noninteractive_element_to_interactive_role -->
                <img src={tech.icon}
                    alt={tech.name}
                    class="tech-logo" 
                    style="background: rgba(255,255,255,0.01); border-radius: 12px;"
                    on:click={() => openTechModal(tech)}
                    on:keydown={(e) => e.key === 'Enter' && openTechModal(tech)}
                    role="button"
                    tabindex="0"/>
            {/each}
        </div>
    </section>

    {#if selectedTech}
     <!-- svelte-ignore a11y_click_events_have_key_events -->
     <!-- svelte-ignore a11y_no_static_element_interactions -->
     <div class="modal-overlay" on:click={closeTechModal}>
            <div class="modal-content" on:click|stopPropagation>
                <button class="modal-close" on:click={closeTechModal}>✕</button>
                <div class="modal-header">
                    <div class="modal-icon">
                        <img src={selectedTech.icon} alt={selectedTech.name} style="width: 100%; height: 100%; object-fit: contain;" />
                    </div>
                    <h3 class="modal-title">{selectedTech.name}</h3>
                </div>
                <p class="modal-description">{selectedTech.description}</p>
            </div>
        </div>
    {/if}

    {#if showCertGallery}
        <!-- svelte-ignore a11y_click_events_have_key_events -->
        <!-- svelte-ignore a11y_no_static_element_interactions -->
        <div class="gallery-overlay" on:click={closeCertGallery}>
            <div class="gallery-content" on:click|stopPropagation on:touchstart={handleTouchStart} on:touchend={handleTouchEnd}>
                <button class="gallery-close" on:click={closeCertGallery}>✕</button>
                <button class="gallery-nav" on:click={prevCert}><span class = "gallery-nav-icon">‹</span></button>
                {#key currentCertIndex}
                <img  
                    
                    src={certifications[currentCertIndex].image} 
                     alt={certifications[currentCertIndex].name} 
                     class="gallery-image" />
                {/key}
                <button class="gallery-nav" on:click={nextCert}><span class = "gallery-nav-icon">›</span></button>
                <div class="gallery-counter">
                    {currentCertIndex + 1} / {certifications.length}
                </div>
            </div>
        </div>
    {/if}

    {#if showEmailModal}
        <!-- svelte-ignore a11y_click_events_have_key_events -->
        <!-- svelte-ignore a11y_no_static_element_interactions -->
        <!-- svelte-ignore a11y_no_static_element_interactions -->
        <div class="modal-overlay" on:click={closeEmailModal}>
            <div class="email-modal-content" on:click|stopPropagation>
                <button class="modal-close" on:click={closeEmailModal}>✕</button>
                <h3 class="email-modal-title">Send Me an Email</h3>
                
                <div class="form-group">
                    <label class="form-label" for="from_name">Your Name</label>
                    <input 
                        type="text" 
                        id="from_name"
                        class="form-input" 
                        bind:value={emailForm.from_name}
                        placeholder="John Doe"
                    />
                </div>

                <div class="form-group">
                    <label class="form-label" for="from_email">Your Email</label>
                    <input 
                        type="email" 
                        id="from_email"
                        class="form-input" 
                        bind:value={emailForm.from_email}
                        placeholder="john@example.com"
                    />
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="subject">Subject</label>
                    <input 
                        type="text" 
                        id="subject"
                        class="form-input" 
                        bind:value={emailForm.subject}
                        placeholder="Enter subject"
                    />
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="body">Message</label>
                    <textarea 
                        id="body"
                        class="form-textarea" 
                        bind:value={emailForm.body}
                        placeholder="Enter your message here..."
                    ></textarea>
                </div>
                
                {#if emailStatus}
                    <div class="email-status" class:success={emailStatus.includes('success')} class:error={!emailStatus.includes('success')}>
                        {emailStatus}
                    </div>
                {/if}
                
                <div class="form-buttons">
                    <button class="cancel-button" on:click={closeEmailModal}>
                        Cancel
                    </button>
                    <button class="send-button" on:click={sendEmail} disabled={sending}>
                        {sending ? 'Sending...' : 'Send Email'}
                    </button>
                </div>
            </div>
        </div>
    {/if}

    <section class="sub-sections">
        <div class="sub-section">
            <h2>Areas of Interest</h2>
            <ul class="interests-list">
                <li>Web Development</li>
                <li>Software Engineering</li>
                <li>Computer Science Education</li>
                <li>Full-Stack Development</li>
            </ul>
        </div>

        <div class="sub-section cert-box" 
             on:click={openCertGallery}
             on:keydown={(e) => e.key === 'Enter' && openCertGallery()}
             role="button"
             tabindex="0">
            <h2>Certifications</h2>
            <p>Click to view all certifications</p>
            {#if certifications.length > 0}
                <img src={certifications[0].image} alt="Certification thumbnail" class="cert-thumbnail" />
            {/if}
        </div>
    </section>

    <section class="contact-section">
        <div class="contact-container">
            <h2 class="contact-title">Get In Touch</h2>
            <p class="contact-subtitle">Have any Inquiries? Feel free to contact me here!</p>
            <button class="email-button" on:click={openEmailModal}>
                Send Me a Message
            </button>
            <div class="contact-info">
                <div class="contact-item">
                    <span class="contact-label">Name</span>
                    <span class="contact-value">Tracy Lansang</span>
                </div>
                <div class="contact-item">
                    <span class="contact-label">Email</span>
                    <span class="contact-value">
                        <a>tjlansang123@gmail.com</a>
                    </span>
                </div>
                <div class="contact-item">
                    <span class="contact-label">Phone</span>
                    <span class="contact-value">0915 973 5829</span>
                </div>
            </div>

            <div class="social-logos">
                <a href="https://github.com/TLDOOM" target="_blank" rel="noopener noreferrer">
                    <img src={gitlogo} alt="GitHub" class="social-logo"/>
                </a>
                <a href="https://www.linkedin.com/in/tracy-lansang-315673297/" target="_blank" rel="noopener noreferrer">
                    <img src={linklogo} alt="LinkedIn" class="social-logo"/>
                </a>
                
            </div>

            
        </div>
    </section>
</div>