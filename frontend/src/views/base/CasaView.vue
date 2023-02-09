<template>
  <v-col cols="12" class="d-flex align-center justify-center">
    <v-img class="ajuste-img" contain height="240" src="@/assets/finance.png" />
  </v-col>
  <v-container class="ajuste-grafico fill-height align-start">
    <v-row>
      <v-col cols="3" class="d-flex align-center justify-center">
        <v-menu v-model="showNovaAnotation" offset-y>
          <template #activator="{ on }">
            <v-btn class="options-btn" color="blue" @click="toggleAnotation">
              <v-icon>mdi-plus-circle-outline</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item @click="addNote">
              <v-list-item-title>Adicionar Nova Anotação</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>

      <v-col cols="3" class="d-flex align-center justify-center">
        <v-btn color="blue" class="profile-btn" @click="toggleProfile">
          <v-icon>mdi-account</v-icon>
        </v-btn>
        <div v-if="showProfile" style="width: 200px">
          <v-card class="caixinha-btn">
            <v-card-title class="headline"> {{ userName }}</v-card-title>
            <v-card-actions>
              <v-list>
                <v-list-item @click="visuPerfil">
                  <v-list-item-title>Perfil</v-list-item-title>
                </v-list-item>
                <v-list-item @click="logoutUser">
                  <v-list-item-title>Deslogar</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card-actions>
          </v-card>
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="10">
        Aqui você pode visualizar os resumos das suas anotações com gráficos.
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
// import LoginView from "../accounts/LoginView.vue"

export default {
  data: () => ({
    showProfile: false,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    showNovaAnotation: false,
    userName: "",
  }),
  methods: {
    addNote() {
      //  direciona pra pagina de criar notações
      this.$router.push("tasks/novanotacao")
    },
    toggleProfile() {
      this.showProfile = !this.showProfile
    },
    toggleAnotation() {
      this.showNovaAnotation = !this.showNovaAnotation
    },
    logoutUser() {
      this.$router.push("accounts/logout")
    },
    visuPerfil() {
      this.$router.push("profile")
    },
  },
  onMounted()=>{
    accountsApi.whoami().then((response)=>{
      if (response.authenticated){
        this.userName = response.user.username
      }
  }
}
</script>

<script setup>
import { onMounted, ref } from "vue"
import axios from "axios"
import accountsApi from "@/api/accounts.api"

const usuario = ref({})

onMounted(() => {
  axios.get("http://localhost/api/accounts/whoami").then((response) => {
    console.log(response.data.user)
    usuario.value = response.data.user
  })
})
</script>

<style>
.options-btn {
  position: absolute;
  top: 20px;
  left: 20px;
}

.profile-btn {
  position: absolute;
  top: 20px;
  right: 20px;
}
.caixinha-btn {
  position: absolute;
  top: 15px;
  right: 100px;
}
.ajuste-img {
  width: 97%;
}
.ajuste-graficos {
  display: flex;
  align-items: flex-start;
}
</style>
