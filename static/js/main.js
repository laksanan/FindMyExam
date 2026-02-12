// Main JavaScript file
console.log('Static files are working! 🎉');

// Example: Add smooth scroll behavior
document.addEventListener('DOMContentLoaded', function () {
    // Add fade-in animation to elements
    const elements = document.querySelectorAll('.fade-in');
    elements.forEach((el, index) => {
        setTimeout(() => {
            el.style.opacity = '1';
        }, index * 100);
    });

    // Example: Dynamic greeting based on time
    const hour = new Date().getHours();
    let greeting = 'สวัสดี';

    if (hour < 12) {
        greeting = 'สวัสดีตอนเช้า';
    } else if (hour < 18) {
        greeting = 'สวัสดีตอนบ่าย';
    } else {
        greeting = 'สวัสดีตอนเย็น';
    }

    console.log(greeting + '! ⏰');
});
