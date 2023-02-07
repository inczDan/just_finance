<template>
  <v-container>
    <v-row align="start" no-gutters style="height: 150px">
      <v-col cols="12">
        <v-img contain height="240" src="@/assets/finance.png" />
        <v-card class="text-center">
          <p class="headline"> Estaremos ansiosos pela sua próxima visita! </p>
          <v-card-text>
            <h2>Tem certeza que deseja finalizar sessão?</h2>
            <p class="ma-10">
              <v-btn :loading="loading" color="blue" class="mr-2" small block @click="logout">
                SIM
              </v-btn>
              <v-btn
                class="my-2"
                block
                color="blue"
                variant="outlined"
                :to="{ name: 'base-casinha' }">
                Voltar
              </v-btn>
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import AccountsApi from "@/api/accounts.api.js"
import { useAppStore } from "@/stores/appStore"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  setup() {
    const appStore = useAppStore()
    const accountsStore = useAccountsStore()
    return { appStore, accountsStore }
  },
  data: () => {
    return {
      loading: false,
    }
  },
  methods: {
    logout() {
      this.loading = true
      AccountsApi.logout()
        .then(() => {
          this.accountsStore.clearLoggedUser()
          this.appStore.showSnackbar("Sessão encerrada!", "warning")
          this.$router.push({ name: "base-home" })
        })
        .finally(() => {
          this.loading = false
        })
    },
  },
}
</script>
