document.addEventListener('DOMContentLoaded', () => {
    fetchCompetitions();

    // Mobile Menu
    const menuToggle = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
            if (navLinks.style.display === 'flex') {
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '60px';
                navLinks.style.right = '0';
                navLinks.style.background = '#fff';
                navLinks.style.width = '100%';
                navLinks.style.padding = '1rem';
                navLinks.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
            }
        });
    }
});

async function fetchCompetitions() {
    const listContainer = document.getElementById('competitions-list');

    try {
        const response = await fetch("https://silicon-synapsis.onrender.com/api/competitions/")


        if (!response.ok) throw new Error('Failed to fetch');

        const competitions = await response.json();
        listContainer.innerHTML = '';

        if (competitions.length === 0) {
            listContainer.innerHTML = '<p>No active competitions at the moment.</p>';
            return;
        }

        competitions.forEach(comp => {
            const card = document.createElement('div');
            card.className = 'competition-card';

            card.innerHTML = `
                <h4>${comp.title}</h4>
                <p>${comp.description.substring(0, 100)}...</p>
                <p class="competition-deadline">
                    Deadline: ${new Date(comp.deadline).toLocaleDateString()}
                </p>
                <a href="submit.html?competition_id=${comp.id}" class="btn-primary">
                    Participate
                </a>
            `;

            listContainer.appendChild(card);
        });

    } catch (error) {
        console.error(error);
        listContainer.innerHTML =
            '<p>Could not load competitions. Make sure backend is running.</p>';
    }
}
