// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
        });
    }
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.nav-links') && !event.target.closest('.menu-toggle')) {
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
            }
        }
    });
    
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId !== '#') {
                e.preventDefault();
                const target = document.querySelector(targetId);
                if (target) {
                    window.scrollTo({
                        top: target.offsetTop - 100,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    initializeImageSlider();
    
    // Ensure responsive height adjustment based on viewport size
    window.addEventListener('resize', adjustSliderHeight);
    adjustSliderHeight();
});

function initializeImageSlider() {
    const slider = document.querySelector('.image-slider');
    if (!slider) return;
    
    const sliderContainer = slider.querySelector('.slider-container');
    const slides = slider.querySelectorAll('.slide');
    const prevBtn = slider.querySelector('.prev-btn');
    const nextBtn = slider.querySelector('.next-btn');
    const dotsContainer = slider.querySelector('.slider-dots');
    
    if (!slides.length) return;
    
    let currentIndex = 0;
    const slideCount = slides.length;
    
    // Create dots
    slides.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });
    
    const dots = slider.querySelectorAll('.dot');
    
    // Function to go to specific slide
    function goToSlide(index) {
        currentIndex = index;
        updateSlider();
    }
    
    // Function to go to next slide
    function nextSlide() {
        currentIndex = (currentIndex + 1) % slideCount;
        updateSlider();
    }
    
    // Function to go to previous slide
    function prevSlide() {
        currentIndex = (currentIndex - 1 + slideCount) % slideCount;
        updateSlider();
    }
    
    // Update slider position and active dot
    function updateSlider() {
        sliderContainer.style.transform = `translateX(-${currentIndex * 100}%)`;
        
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
    }
    
    // Event listeners
    prevBtn.addEventListener('click', prevSlide);
    nextBtn.addEventListener('click', nextSlide);
    
    // Auto-slide every 5 seconds
    let interval = setInterval(nextSlide, 5000);
    
    // Pause auto-slide when hovering over slider
    slider.addEventListener('mouseenter', () => {
        clearInterval(interval);
    });
    
    slider.addEventListener('mouseleave', () => {
        interval = setInterval(nextSlide, 5000);
    });
    
    // Add touch support for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    
    sliderContainer.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });
    
    sliderContainer.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    }, { passive: true });
    
    function handleSwipe() {
        if (touchEndX < touchStartX) {
            // Swipe left
            nextSlide();
        } else if (touchEndX > touchStartX) {
            // Swipe right
            prevSlide();
        }
    }
    
    // Function to adjust slider height
    function adjustSliderHeight() {
        const slider = document.querySelector('.image-slider');
        if (!slider) return;
        
        // You can add responsive height breakpoints here if needed
        // For example:
        if (window.innerWidth <= 768) {
            slider.style.height = '300px';
        } else {
            slider.style.height = '400px';
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    initializeImageSlider();
});

function initializeImageSlider() {
    const slider = document.querySelector('.image-slider');
    if (!slider) return;
    
    const sliderContainer = slider.querySelector('.slider-container');
    const slides = slider.querySelectorAll('.slide');
    const prevBtn = slider.querySelector('.prev-btn');
    const nextBtn = slider.querySelector('.next-btn');
    const dotsContainer = slider.querySelector('.slider-dots');
    
    if (!slides.length) return;
    
    let currentIndex = 0;
    const slideCount = slides.length;
    
    // Create dots
    slides.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });
    
    const dots = slider.querySelectorAll('.dot');
    
    // Function to go to specific slide
    function goToSlide(index) {
        currentIndex = index;
        updateSlider();
    }
    
    // Function to go to next slide
    function nextSlide() {
        currentIndex = (currentIndex + 1) % slideCount;
        updateSlider();
    }
    
    // Function to go to previous slide
    function prevSlide() {
        currentIndex = (currentIndex - 1 + slideCount) % slideCount;
        updateSlider();
    }
    
    // Update slider position and active dot
    function updateSlider() {
        sliderContainer.style.transform = `translateX(-${currentIndex * 100}%)`;
        
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
    }
    
    // Event listeners
    prevBtn.addEventListener('click', prevSlide);
    nextBtn.addEventListener('click', nextSlide);
    
    // Auto-slide every 5 seconds
    let interval = setInterval(nextSlide, 5000);
    
    // Pause auto-slide when hovering over slider
    slider.addEventListener('mouseenter', () => {
        clearInterval(interval);
    });
    
    slider.addEventListener('mouseleave', () => {
        interval = setInterval(nextSlide, 5000);
    });
    
    // Add touch support for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    
    sliderContainer.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });
    
    sliderContainer.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    }, { passive: true });
    
    function handleSwipe() {
        if (touchEndX < touchStartX) {
            // Swipe left
            nextSlide();
        } else if (touchEndX > touchStartX) {
            // Swipe right
            prevSlide();
        }
    }
}

// Add responsive navigation styles
document.head.insertAdjacentHTML('beforeend', `
<style>
@media (max-width: 768px) {
    .nav-links {
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background-color: white;
        flex-direction: column;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transform: translateY(-100%);
        opacity: 0;
        pointer-events: none;
        transition: all 0.3s ease;
    }
    
    .nav-links.active {
        transform: translateY(0);
        opacity: 1;
        pointer-events: auto;
    }
}
</style>
`);



// Slideshow functionality
// Slideshow functionality for many slides
    let slideIndex = 1;
    const slides = document.getElementsByClassName("slide");
    const dots = document.getElementsByClassName("dot");
    const thumbnails = document.getElementsByClassName("thumbnail");
    let slideInterval;
    
    // Initialize
    showSlides(slideIndex);
    startSlideShow();
    
    function plusSlides(n) {
        clearInterval(slideInterval);
        showSlides(slideIndex += n);
        startSlideShow();
    }
    
    function currentSlide(n) {
        clearInterval(slideInterval);
        showSlides(slideIndex = n);
        startSlideShow();
    }
    
    function showSlides(n) {
        // Handle wrap-around
        if (n > slides.length) { slideIndex = 1 }
        if (n < 1) { slideIndex = slides.length }
        
        // Hide all slides
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        
        // Update dot indicators
        for (let i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        
        // Update thumbnail highlights
        for (let i = 0; i < thumbnails.length; i++) {
            thumbnails[i].classList.remove("active-thumb");
        }
        
        // Show current slide and update indicators
        slides[slideIndex-1].style.display = "block";
        dots[slideIndex-1].className += " active";
        if (thumbnails[slideIndex-1]) {
            thumbnails[slideIndex-1].classList.add("active-thumb");
        }
    }
    
    function startSlideShow() {
        clearInterval(slideInterval);
        slideInterval = setInterval(() => {
            plusSlides(1);
        }, 5000);
    }
    
    // Pause on hover
    document.querySelector('.slideshow-container').addEventListener('mouseenter', () => {
        clearInterval(slideInterval);
    });
    
    document.querySelector('.slideshow-container').addEventListener('mouseleave', startSlideShow);