<template>
  <div id="app">
    <!-- Navigation Bar -->
    <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/matchLoadouts">Match Loadouts</router-link>
      <a @click="redirectToGithub" class="github">GitHub</a>
      <a @click="redirectToDiscord" class="github">Discord</a>
      <a @click="toggleThemeSelector">Themes</a>
    </div>

    <!-- Theme Selector -->
    <div id="theme-selector" v-if="showThemeSelector">
      <h3>Select a Theme</h3>
      <button @click="setTheme('dark-neon')">Dark-Neon</button>
      <button @click="setTheme('valorant-ui')">Clean Valorant-Inspired UI</button>
      <button @click="setTheme('edgy-minimalist')">Edgy Minimalist</button>
    </div>

    <!-- Main Content -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      currentTheme: "valorant-ui", // Default to Valorant-inspired UI
      showThemeSelector: false,
    };
  },
  methods: {
    redirectToGithub() {
      window.open("https://github.com/isaacKenyon/VALORANT-rank-yoinker");
    },
    redirectToDiscord() {
      window.open("https://discord.gg/HeTKed64Ka");
    },
    toggleThemeSelector() {
      this.showThemeSelector = !this.showThemeSelector;
    },
    setTheme(theme) {
      this.currentTheme = theme;
      this.applyTheme();
    },
    applyTheme() {
      const body = document.body;
      body.className = ""; // Reset all theme classes
      body.classList.add(this.currentTheme);
    },
  },
  mounted() {
    this.applyTheme(); // Apply the default theme on load
  },
};
</script>

<style>
/* General Reset */
body {
  margin: 0;
  padding: 0;
  font-family: "Inter", sans-serif;
}

/* App Container */
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  height: 100vh;
  text-align: center;
  color: white;
}

/* Navigation Bar */
#nav {
  width: 100%;
  background-color: var(--nav-background, #1e1e2f);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px 0;
}

#nav a {
  color: var(--text-color, #ff4655);
  font-weight: bold;
  text-decoration: none;
  margin: 0 15px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

#nav a.router-link-exact-active {
  border-bottom: 2px solid var(--highlight-color, #ff4655);
}

#nav a:hover {
  color: var(--hover-text-color, #e0e0e0);
  border-bottom: 2px solid var(--highlight-color, #ff4655);
}

/* Theme Selector */
#theme-selector {
  position: fixed;
  top: 15%;
  background: var(--modal-background, rgba(30, 30, 47, 0.9));
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 15px var(--box-shadow-color, rgba(255, 70, 85, 0.5));
  color: var(--text-color, white);
  text-align: center;
  z-index: 10;
}

#theme-selector button {
  background: var(--button-background, transparent);
  border: 2px solid var(--text-color, white);
  color: var(--text-color, white);
  padding: 10px 20px;
  margin: 10px;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease;
}

#theme-selector button:hover {
  background: var(--highlight-color, #ff4655);
  color: var(--hover-text-color, black);
}

/* Themes */
body.dark-neon {
  --nav-background: #0d0f1a;
  --text-color: #00ffcc;
  --highlight-color: #00ffcc;
  --modal-background: rgba(13, 15, 26, 0.95);
  --box-shadow-color: rgba(0, 255, 204, 0.5);
  --button-background: #002244;
  --hover-text-color: #002b36;
  background: linear-gradient(135deg, #001a33, #000d1a);
  color: #00ffcc; /* Bright cyan for contrast */
  text-shadow: 0 0 5px #00ffcc;
}

body.valorant-ui {
  --nav-background: #1e1e2f;
  --text-color: #ff4655;
  --highlight-color: #ff4655;
  --modal-background: rgba(30, 30, 47, 0.9);
  --box-shadow-color: rgba(255, 70, 85, 0.5);
  --button-background: #444;
  --hover-text-color: white;
  background: linear-gradient(135deg, #1e1e2f, #121212);
  color: #ff4655;
}

body.edgy-minimalist {
  --nav-background: black;
  --text-color: white;
  --highlight-color: white;
  --modal-background: rgba(0, 0, 0, 0.9);
  --box-shadow-color: rgba(255, 255, 255, 0.2);
  --button-background: #000;
  --hover-text-color: #c0c0c0;
  background: linear-gradient(135deg, #121212, #000000);
  color: #e0e0e0; /* Softer white for reduced strain */
}
/* Theme Variables */
body.dark-neon {
  --modal-background: #0d0f1a;
  --player-card-bg: #222;
  --text-primary: #00ffcc;
  --border-color: #444;
}

body.valorant-ui {
  --modal-background: #1e1e2f;
  --player-card-bg: #2c2c3f;
  --text-primary: #ff4655;
  --border-color: #555;
}

body.edgy-minimalist {
  --modal-background: black;
  --player-card-bg: #222;
  --text-primary: white;
  --border-color: #666;
}
</style>
