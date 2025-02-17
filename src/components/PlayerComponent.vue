<template>
    <div
      class="basicdiv"
      :class="{ blueTeam: PlayerLoadout.Team === 'Blue', otherTeam: PlayerLoadout.Team !== 'Blue' }"
      @click="$emit('openModal', PlayerLoadout)">
      <img class="agent_img" :src="PlayerLoadout.Agent" :alt="PlayerLoadout.AgentArtworkName" />
      
      
      <div id="player-names"></div>
      <button class="btn btn--light" :class="{ btn_blue: blue }">
        <span class="btn__inner" :class="{ btn_blue: blue }">
          <span class="btn__slide"></span>
          <span class="btn__content">{{ PlayerLoadout.Name}}</span>
        </span>
      </button>
  
      <div class="weapon_icons">
        <img
          class="weapon_img"
          :src="PlayerLoadout.Weapons['9c82e19d-4575-0200-1a81-3eacf00cf872'].skinDisplayIcon"
          :alt="PlayerLoadout.Weapons['9c82e19d-4575-0200-1a81-3eacf00cf872'].skinDisplayName"
        />
        <img
          class="weapon_img"
          :src="PlayerLoadout.Weapons['ee8e8d15-496b-07ac-e5f6-8fae5d4c7b1a'].skinDisplayIcon"
          :alt="PlayerLoadout.Weapons['ee8e8d15-496b-07ac-e5f6-8fae5d4c7b1a'].skinDisplayName"
        />
        <img
          class="weapon_img"
          :src="PlayerLoadout.Weapons['e336c6b8-418d-9340-d77f-7a9e4cfe0702'].skinDisplayIcon"
          :alt="PlayerLoadout.Weapons['e336c6b8-418d-9340-d77f-7a9e4cfe0702'].skinDisplayName"
        />
      </div>
    </div>
  </template>
  
  <script>
  
  
  
  
  export default {
      props: ["PlayerLoadout"],
      data() {
          return {
              blue: this.PlayerLoadout.Team == "Blue"
          }
      },
      mounted() {
      // Reference the container div
      const playerNamesContainer = document.getElementById("player-names");
  
      // Clear previous content (if any)
      playerNamesContainer.innerHTML = "";
  
      // Check if Players exists in PlayerLoadout
      if (this.PlayerLoadout.Players && Array.isArray(this.PlayerLoadout.Players)) {
        // Iterate through Players and create <h1> elements
        this.PlayerLoadout.Players.forEach((player) => {
          const playerNameElement = document.createElement("h1");
          playerNameElement.textContent = player.Name || "Unknown Player";
          playerNamesContainer.appendChild(playerNameElement);
        });
      } else {
        // Handle case where Players is not defined or not an array
        const noPlayersMessage = document.createElement("h1");
        noPlayersMessage.textContent = "No players found";
        playerNamesContainer.appendChild(noPlayersMessage);
      }
    },
  }
  </script>
  
  <style>
      .basicdiv {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        margin: 10px auto;
        background-color: var(--background-color, #111);
        border: 2px solid var(--border-color, #444);
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        width: 100%;
        max-width: 600px;
        transition: transform 0.3s, background-color 0.3s;
      }
  
      .basicdiv:hover {
        transform: scale(1.05);
        background-color: var(--hover-background-color, #222);
      }
  
      .player {
          display: flex;
          flex-direction: column;
          align-items: center;
          background-color: var(--box);
          box-sizing: border-box;
          width: 100%;
          margin: 20px auto;
          padding: 15px;
          border-radius: 10px;
          border: solid 2.5px black;
          cursor: pointer;
          transition-duration: 0.3s;
      }
  
      .player:hover  {
          background-color: var(--box-200);
          border-radius: 20px;
      }
  
      .player_name {
          margin-top: 10px;
          font-size: 1.5em;
          color: var(--highlight-color);
      }
  
      .btn {
          -moz-appearance: none;
          -webkit-appearance: none;
          appearance: none;
          border: none;
          background: none;
          padding: 0;
          color: var(--button-text-color);
          cursor: pointer;
          position: relative;
          padding: 8px;
          margin-bottom: 20px;
          text-transform: uppercase;
          font-weight: bold;
          font-size: 14px;
          transition: all .15s ease;
      }
  
      .btn::before,
      .btn::after {
          content: '';
          display: block;
          position: absolute;
          right: 0; left: 0;
          height: calc(50% - 5px);
          border: 1px solid var(--border-color);
          transition: all .15s ease;
      }
  
      .btn::before {
          top: 0;
          border-bottom-width: 0;
      }
  
      .btn::after {
          bottom: 0;
          border-top-width: 0;
      }
  
      .btn:active,
      .btn:focus {
          outline: none;
      }
  
      .btn:active::before,
      .btn:active::after {
          right: 3px;
          left: 3px;
      }
  
      .btn:active::before {
          top: 3px;
      }
  
      .btn:active::after {
          bottom: 3px;
      }
  
      .btn__inner {
          position: relative;
          display: block;
          padding: 20px 30px;
          background-color: var(--button-background-color);
          overflow: hidden;
          box-shadow: inset 0px 0px 0px 1px var(--button-inner-border-color);
      }
  
      .btn_blue {
          color: #1971ff;
          box-shadow: inset 0px 0px 0px 1px #1971ff;
      }
  
      .btn__inner::before {
          content: '';
          display: block;
          position: absolute;
          top: 0; left: 0;
          width: 2px;
          height: 2px;
          background-color: var(--button-bits-color);
      }
  
      .btn__inner::after {
          content: '';
          display: block;
          position: absolute;
          right: 0; bottom: 0;
          width: 4px;
          height: 4px;
          background-color: var(--button-bits-color);
          transition: all .2s ease;
      }
  
      .btn__slide {
          display: block;
          position: absolute;
          top: 0; bottom: -1px; left: -8px;
          width: 0;
          background-color: var(--highlight-color);
          transform: skew(-15deg);
          transition: all .2s ease;
      }
  
      .btn__content {
          position: relative;
      }
  
      .btn:hover {
          color: var(--button-text-color-hover);
      }
  
      .btn:hover .btn__slide {
          width: calc(100% + 15px);
      }
  
      .btn:hover .btn__inner::after {
          background-color: var(--button-bits-color-hover);
      }
  
      .btn--light {
          --button-background-color: var(--background-color);
          --button-text-color: var(--highlight-color);
          --button-inner-border-color: var(--highlight-color);
          --button-text-color-hover: #ece8e1;
          --button-bits-color-hover: #ece8e1;
      }
  
      .agent_img {
          margin: 10px auto;
          height: 72px;
          border-radius: 50px;
          border: solid 2px var(--border-color);
      }
  
      .weapon_icons {
          display: flex;
          justify-content: center;
          gap: 10px;
          margin-top: 10px;
      }
  
      .weapon_img {
          height: 50px;
          border-radius: 5px;
          background-color: var(--background-color);
          border: solid 1px var(--border-color);
          padding: 5px;
          transition: transform 0.2s;
      }
  
      .weapon_img:hover {
          transform: scale(1.1);
      }
  </style>
  