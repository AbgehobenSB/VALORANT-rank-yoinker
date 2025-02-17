<template>
    <div class="modal-backdrop" @click.self="$emit('closeModal')">
        <div class="modal">
              <div class="flexbox flexbox-column">
                  
                  <div class="flexbox">
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="false" weaponName="none"/>
                      <!-- <div class="box flex-1"></div> -->
                      <div class="box flex-1 player-card">
                          <div class="levelDiv">
                              <span class="levelText">{{ this.PlayerLoadout.Level }}</span>
                          </div>
  
  
  
                          <div class="nameDiv">
                              <span class="nameText">{{ this.PlayerLoadout.AgentArtworkName.substring(0, this.PlayerLoadout.AgentArtworkName.length - 7) }}</span>
                          </div>
                        
  
  
                          <div class="titleDiv">
                              <span class="titleText">{{ this.PlayerLoadout.Title }}</span>
                          </div>
                          <img v-if="PlayerCardIMG!==null" :src="PlayerCardIMG" alt="PlayerCard" class="PlayerCard">
                      </div>
  
                      <img :src="AgentArtworkPath" :alt="this.PlayerLoadout.AgentArtworkName" class="img-agent">
  
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="true" weaponName="Classic"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Stinger"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Bulldog"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Marshal"/>
                  </div>
                  <div class="flexbox">
                    <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="false" weaponName="none"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="true" weaponName="Shorty"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Spectre"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Guardian"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Outlaw"/>
      
                  </div>
                  <div class="flexbox">
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="true" weaponName="Spray1"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="true" weaponName="Frenzy"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Bucky"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Phantom"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Operator"/>
                  </div>
                  <div class="flexbox">
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="true" weaponName="Spray2"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="true" weaponName="Ghost"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Judge"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Vandal"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Ares"/>
                      
                  </div>
                  <div class="flexbox">
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="true" weaponName="Spray3"/>
                      
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="true" weaponName="Sheriff"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="false" weaponName="none"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="false" weaponName="none"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Odin"/>
                  </div>
                  <div class="flexbox">
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="true" weaponName="Spray4"/>
                      
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="false" :visible="false" weaponName="none"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="false" weaponName="none"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="false" weaponName="none"/>
                      <WeaponBox :PlayerLoadout="PlayerLoadout" :flex2="true" :visible="true" weaponName="Melee"/>
                  </div>
  
  
              </div>
            
            <!-- <p v-for="spray in PlayerLoadout.Sprays" :key="spray.displayName"> -->
                <!-- <img :src="spray.displayIcon" :alt="spray.displayName"> -->
            <!-- </p> -->
            <!-- <p>{{ PlayerLoadout }}</p> -->
        </div>
    </div>
  </template>
  <script>
  import WeaponBox from "./WeaponBox.vue";
  
  export default {
    props: ["PlayerLoadout"],
    components: { WeaponBox },
    data() {
      return {
        PlayerCardIMG: null, // Holds player card image
        AgentArtworkPath: null, // Holds the URL for the agent's artwork
      };
    },
    methods: {
      async fetchAgentArtwork() {
        try {
          const response = await fetch("https://valorant-api.com/v1/agents");
          const data = await response.json();
  
          // Check if data.data is an array
          if (Array.isArray(data.data)) {
            console.log("Agents Array from API:", data.data);
  
            // Normalize the name from PlayerLoadout and remove "Artwork" suffix
            const agentName = this.PlayerLoadout.AgentArtworkName.replace("Artwork", "").toLowerCase();
  
            // Find the agent that matches the processed name
            const agent = data.data.find(
              (agent) => agent.displayName.toLowerCase() === agentName
            );
  
            if (agent) {
              console.log("Matched Agent:", agent);
  
              if (agent.fullPortrait) {
                this.AgentArtworkPath = agent.fullPortrait;
                console.log("Agent Artwork Path:", agent.fullPortrait);
              } else {
                console.error("No full portrait available for agent:", agent.displayName);
                this.AgentArtworkPath = "default-agent-image.png";
              }
            } else {
              console.error("No matching agent found for:", agentName);
              this.AgentArtworkPath = "default-agent-image.png";
            }
          } else {
            console.error("Unexpected API data format:", data);
            this.AgentArtworkPath = "default-agent-image.png";
          }
        } catch (error) {
          console.error("Error fetching agent artwork:", error);
          this.AgentArtworkPath = "default-agent-image.png"; // Fallback image
        }
      },
      debugPlayerLoadout() {
        console.log("PlayerLoadout Debug Info:", this.PlayerLoadout);
        console.log("PlayerCard Image Path:", this.PlayerCardIMG);
        console.log("Agent Artwork Path:", this.AgentArtworkPath);
      },
    },
    mounted() {
      this.PlayerCardIMG = this.PlayerLoadout.PlayerCard; // Assign player card image
      this.fetchAgentArtwork(); // Fetch agent artwork dynamically
  
      // Debugging PlayerLoadout after setup
      this.debugPlayerLoadout();
    },
  };
  </script>

<style>
/* Modal Styling */
.modal {
  position: relative;
  width: 60%; /* Adjust width to fit content */
  max-width: 1600px; /* Cap the width */
  height: auto; /* Automatically adjust height */
  padding: 20px;
  margin: 200px auto; /* Center the modal */
  background-color: var(--modal-background, #1e1e2f);
  border-radius: 10px;
  border: 2px solid var(--border-color, black);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

/* Modal Backdrop */
.modal-backdrop {
  padding: 0;
  margin: 0;
  top: 0;
  position: fixed;
  background: rgba(0, 0, 0, 0.6);
  width: 100%;
  height: 100%;
  z-index: 1000;
}

/* Player Card */
.player-card {
  z-index: 1;
  position: absolute;
  width: 165px;
  left: 20px;
  height: 286px;
  background-color: var(--player-card-bg, #2c2c3f);
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  overflow: hidden;
}

.PlayerCard {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

/* Agent Artwork */
.img-agent {
  position: absolute;
  top: 0;
  bottom: -10%;
  margin: auto;
  height: 90%;
  z-index: 0;
  opacity: 0.3;
  pointer-events: none;
}

/* Level Display */
.levelDiv {
  position: absolute;
  width: 50%;
  height: 10%;
  top: 2%;
  left: 25%;
  background-color: var(--background-color, #444);
  border-radius: 50px;
  border: 2px solid var(--border-color, black);
  text-align: center;
  box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.2);
}

.levelText {
  font-size: 1.5em;
  color: var(--text-primary, white);
  font-weight: bold;
  line-height: 1.5;
}

/* Title Display */
.titleDiv {
  position: absolute;
  width: 100%;
  height: 5%;
  bottom: 28%;
  background-color: rgba(0, 0, 0, 0.6); /* Black bar */
  text-align: center;
}

.titleText {
  font-size: 0.8em;
  color: var(--text-primary, #e0e0e0);
  font-weight: bold;
  line-height: 1.5;
}

/* Name Display */
.nameDiv {
  position: absolute;
  width: 100%;
  height: 5%;
  bottom: 33%;
  background-color: rgba(0, 0, 0, 0.6); /* Black bar */
  text-align: center;
}

.nameText {
  font-size: 0.8em;
  color: var(--text-primary, #e0e0e0);
  font-weight: bold;
  line-height: 1.5;
}
</style>
