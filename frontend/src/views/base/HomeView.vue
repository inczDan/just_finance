<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      
      <blockquote class="blockquote text-h5">
        <h1 class="text-h2 font-weight-bold">Just Finance</h1>
        <br>
        &#8220;Controle o mundo, começando pelo seu bolso.&#8221;
        <footer>
          <small>
            <em>&mdash; Daniel A. Matos &mdash;</em>
          </small>
        </footer>
      </blockquote>

      <div class="text-body-1 mb-n1 pt-4">Bem-vindo(a) a sua mais nova jornada </div>
      <div class="py-6 ajuste-btn" />
      <v-row class="d-flex align-center justify-center ">
        <v-col cols="auto" class="ajuste-btn">
          <v-btn
            color="blue"
            :to="{ name: 'base-getstarted' }"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="my-4">
            <v-icon icon="mdi-form-select" size="large" start />
            Cadastre-se
          </v-btn>
          <v-btn
            v-if="!loggedUser"
            color="blue"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-login' }"
            class="my-4">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Login
          </v-btn>
          <v-btn
            v-else
            color="blue"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-logout' }">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Logout
          </v-btn>
          <v-btn
            v-if="loggedUser"
            color="blue"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'tasks-list' }"
            class="my-4">
            <v-icon icon="mdi-folder-star-multiple" size="large" start />
            tarefas
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
}
</script>

<style>
.ajuste-btn{
  display: flex;
  width:550px;
  justify-content: space-evenly;
  max-width: 68%;
}
</style>