<template>
    <div :class="{ box: visible,
                  'box-invisible': !visible,
                  'flex-2': flex2,
                  'flex-1': !flex2 }"
                  :id="weaponName">
        <img v-if="imgPath!==null" :src="imgPath" :alt="weaponName" :class="{sprayIMG: isSpray, 'weaponIMG': !isSpray}">
        <div v-if="imgPath!==null" class="placeholderDiv">
          <span class="placeholderText">{{skinDisplayName}}</span>
        </div>
        <img v-if="buddyIMG!==null" :src="buddyIMG" alt="skin_buddy" class="buddyIMG">
    </div>
  </template>
  
  <script>
  export default {
    props: ["PlayerLoadout", "flex2", "visible", "weaponName"],
    mounted() {
      // Handle Weapons
      if (!this.weaponName.startsWith("Spray")) {
        for (let weaponID of Object.keys(this.PlayerLoadout.Weapons)) {
          let weapon = this.PlayerLoadout.Weapons[weaponID];
          if (weapon.weapon === this.weaponName) {
            console.error(`Weapon Found:`, weapon);
            this.imgPath = weapon.skinDisplayIcon || null;
            this.skinDisplayName = weapon.skinDisplayName || "Unknown Weapon";
            if (weapon.buddy_displayIcon) {
              this.buddyIMG = weapon.buddy_displayIcon;
            }
            return; // Exit once the weapon is processed
          }
        }
        console.error(`Weapon not found for: ${this.weaponName}`);
        this.imgPath = null;
        this.skinDisplayName = "No Weapon Found";
        return;
      }
  
      // Handle Sprays and Expressions
      if (this.weaponName.startsWith("Spray")) {
        let index = parseInt(this.weaponName.substring(5, 6)) - 1; // Extract spray index
        console.error("Sprays Output:", this.PlayerLoadout.Sprays);
        console.error("Expressions Output:", this.PlayerLoadout.Expressions);
  
        // Check if an Expression exists for this slot
        let expression = this.PlayerLoadout.Expressions?.[index];
        if (expression?.displayIcon) {
          console.error(`Expression Found at index ${index}:`, expression);
          this.imgPath = expression.displayIcon;
          this.isFlex = true;
          this.skinDisplayName = expression.displayName || "Unknown Expression";
        } else {
          // Fallback to Spray data
          let spray = this.PlayerLoadout.Sprays?.[index];
          if (spray) {
            console.error(`Spray Found at index ${index}:`, spray);
            this.imgPath = spray.displayIcon;
            this.isSpray = true;
            this.skinDisplayName = spray.displayName || "Unknown Spray";
          } else {
            console.error(`No Spray or Expression found at index ${index}`);
            this.imgPath = null;
            this.skinDisplayName = "No Spray or Expression";
          }
        }
      }
    },
    data() {
      return {
        imgPath: null, // Path for the item's image
        isSpray: false, // Whether the item is a spray
        isFlex: false, // Whether the item is an expression (Flex)
        skinDisplayName: null, // Name of the spray or expression
        buddyIMG: null, // Image for the buddy if available
      };
    },
  };
  </script>
  
  
  
  
  <style>
      .box {
          box-sizing: border-box;
          position: relative;
          width: 100px; /* Adjusted size from old project */
          height: 130px; /* Adjusted size from old project */
          background-color: var(--inventory-slot, #2c2c3f); /* Fallback color added */
          border: 1px solid var(--border-color, #868686); /* Fallback color added */
          border-radius: 5px; /* Adjusted radius from old project */
          margin: 0 7px; /* Adjusted margin from old project */
          transition-duration: 0.1s;
          cursor: pointer;
      }
  
      .box:hover {
          padding: 5px; /* Adjusted padding from old project */
          background-color: var(--inventory-slot-hover, #444);
      }
  
      .box:hover .placeholderDiv {
          padding: 0 5px; /* Adjusted padding from old project */
          left: -5px; /* Adjusted position from old project */
          margin: 111px 0; /* Adjusted margin from old project */
      }
  
      .box-invisible {
          width: 100px; /* Adjusted size from old project */
          height: 130px; /* Adjusted size from old project */
          border-radius: 5px; /* Adjusted radius from old project */
          margin: 0 8px; /* Adjusted margin from old project */
      }
  
      .flexbox {
          display: flex;
          flex-wrap: wrap;
          justify-content: space-around;
      }
      
      .flexbox-column {
          height: 900px; /* Adjusted height from old project */
          flex-direction: column;
      }
  
      .flex-1 {
          flex: 1;
      }
  
      .flex-2 {
          flex: 2;
      }
  
      .weaponIMG {
          position: absolute;
          max-width: 100%; /* Ensures the image does not overflow */
          max-height: 100%; /* Adjusted size from old project */
          object-fit: contain; /* Preserves aspect ratio */
          top: 0;
          bottom: 0;
          left: 0;
          right: 0;
          margin: auto; /* Centers the image */
          padding: 3px; /* Adjusted padding from old project */
          box-sizing: border-box;
      }
  
      .sprayIMG {
          position: absolute;
          width: 75%; /* Adjusted size from old project */
          top: 0;
          bottom: 0;
          left: 0;
          right: 0;
          margin: auto;
          box-sizing: border-box;
          border-radius: 10px; /* Adjusted radius from old project */
      }
      
      .placeholderDiv {
          position: relative;
          background-color: var(--placeholder-div, rgba(0, 0, 0, 0.7)); /* Dynamic background */
          z-index: 2;
          width: 100%; /* Adjusted size from old project */
          height: 10%; /* Adjusted size from old project */
          margin: 115px 0; /* Adjusted margin from old project */
          left: 0;
          transition-duration: 0.1s;
      }
  
      .placeholderText {
          position: absolute;
          font-size: 0.8em; /* Adjusted size from old project */
          font-weight: bold;
          left: 0;
          right: 0;
          margin: auto;
          top: -1px; /* Adjusted position from old project */
          color: var(--placeholder-text, #ffffff); /* Dynamic text color */
          transition-duration: 0.1s;
      }
  
      .box:hover .placeholderText {
          top: -2px; /* Adjusted position from old project */
      }
  
      .buddyIMG {
          z-index: 3;
          position: absolute;
          bottom: 2%; /* Adjusted position from old project */
          left: 0;
          width: 18%; /* Adjusted size from old project */
      }
  </style>
  