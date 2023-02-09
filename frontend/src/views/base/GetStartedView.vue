<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <v-img contain height="240" src="@/assets/finance.png" />
      <v-card>
        <v-card-title class="headline">Realize seu cadastro </v-card-title>
        <v-card-text>
          <v-form ref="form">
            <v-text-field v-model="username" label="Nome" :rules="nameRules" />
            <v-text-field v-model="email" label="Email" :rules="emailRules" />
            <v-text-field v-model="password" label="Senha" type="password" :rules="passwordRules" />
            <v-text-field
              v-model="confirmPassword"
              label="Confirme a Senha"
              type="password"
              :rules="confirmPasswordRules" />
            <v-card-actions></v-card-actions>
            <div class="ajuste-btn">
              <v-btn color="blue" @click="register()"> Registrar </v-btn>
              <v-btn color="blue" :to="{ name: 'base-home' }"> Início </v-btn>
            </div>
            <hr class="my-3" />
          </v-form>
        </v-card-text>
      </v-card>
    </v-responsive>
  </v-container>
</template>

<script>
import AccountsApi from "@/api/accounts.api.js"
import { useAppStore } from "@/stores/appStore"
import { useAccountsStore } from "@/stores/accountsStore"
import { responseError } from "@/api/config"

export default {
  setup() {
    const appStore = useAppStore()
    const accountsStore = useAccountsStore()
    return { appStore, accountsStore }
  },
  data: () => ({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
    nameRules: [(v) => !!v || "Nome é obrigatório"],
    emailRules: [
      (email) => !!email || "Email é obrigatório",
      (v) => /.+@.+\..+/.test(v) || "Email inválido",
    ],
    passwordRules: [(v) => !!v || "Senha é obrigatória"],
    confirmPasswordRules: [
      (v) => !!v || "Confirme a senha",
      //easter egg {se voce leu até aqui, bora comer coxinha}
      (v) => v === this.password || "Senhas não coincidem",
    ],
  }),
  methods: {
    register() {
      if (this.$refs.form.validate()) {
        AccountsApi.getregister(this.username, this.email, this.password)
          .then((response) => {
            if (response.error) {
              this.appStore.showSnackbar("Erro ao registrar usuario", responseError)
            } else if (response.success) {
              this.$router.push({ name: "accounts-login" })
              console.log("Usuário registrado com sucesso.")
            }
          })
          .catch((error) => {
            console.error("Erro ao registrar usuário:", error)
          })
      }
    },
  },
}
</script>

<style>
.ajuste-btn {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-evenly;
  width: 100%;
  max-width: 100%;
}
</style>
