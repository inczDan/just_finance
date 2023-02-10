import { updateProfilePicture } from "@/api/accounts.api"
<template>
  <v-col cols="1">
    <v-btn
      block
      size="small"
      rounded="pill"
      color="blue"
      :to="{ name: 'base-casinha' }"
      @click="login">
      <v-icon>mdi-arrow-left</v-icon>
    </v-btn>
  </v-col>
  <v-container>
    <v-row align="center" no-gutters>
      <v-col cols="12" class="d-flex align-center justify-center">
        <v-avatar class="ma-3" size="200">
          <v-img height="200px" :src="profilePicture" />
        </v-avatar>
      </v-col>
      <v-col cols="12" class="d-flex align-center justify-center mt-5">
        <input type="file" accept="image/jpeg" @change="sobeFoto" />
      </v-col>
    </v-row>
    <br /><br /><br />
    <v-row align="center" no-gutters>
      <v-col cols="12"></v-col>
    </v-row>
    <v-col class="d-flex align-center justify-center">
      <v-card class="elevation-12">
        <v-card-title class="headline">Nome: {{ userName }} </v-card-title>
        <v-card-text>
          <p>Email: {{ userEmail }}</p>
        </v-card-text>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
import updateProfilePicture from "@/api/accounts.api"
import accountsApi from "@/api/accounts.api"

export default {
  data() {
    return {
      userName: "",
      userEmail: "",
      profilePicture: "",
    }
  },
  mounted() {
    accountsApi.whoami().then((response) => {
      if (response.authenticated) {
        this.userName = response.user.username
        this.userEmail = response.user.email
      }
    })
  },
  methods: {
    sobeFoto(event) {
      const input = event.target
      if (input.files && input.files[0]) {
        const reader = new FileReader()
        reader.onload = (e) => {
          this.profilePicture = e.target.result
          this.saveProfilePicture()
        }
        reader.readAsDataURL(input.files[0])
      }
    },
    async saveProfilePicture() {
      try {
        const response = await updateProfilePicture(this.picture)
        console.log(response)
      } catch (error) {
        console.error(error)
      }
    },
  },
}
</script>
