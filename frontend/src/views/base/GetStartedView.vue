<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <v-img contain height="240" src="@/assets/finance.png" />
      <v-card>
        <v-card-title class="headline">Realize seu cadastro </v-card-title>
        <v-card-text>
          <v-form ref="form">
        <v-text-field
          label="Nome"
          v-model="name"
          :rules="nameRules"
        />
        <v-text-field
          label="Email"
          v-model="email"
          :rules="emailRules"
        />
        <v-text-field
          label="Senha"
          type="password"
          v-model="password"
          :rules="passwordRules"
        />
        <v-text-field
          label="Confirme a Senha"
          type="password"
          v-model="confirmPassword"
          :rules="confirmPasswordRules"
        />
        <v-card-actions></v-card-actions>
        <div class="ajuste-btn">
          <v-btn @click="register" :to="{name: 'accounts-login'}" color="blue"> Registrar </v-btn>
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
import axios from 'axios';

export default {
  data: () => ({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
    nameRules: [
      name => !!name || 'Nome é obrigatório',
    ],
    emailRules: [
      email => !!email || 'Email é obrigatório',
      v => /.+@.+\..+/.test(v) || 'Email inválido',
    ],
    passwordRules: [
      password => !!password || 'Senha é obrigatória',
    ],
    confirmPasswordRules: [
      v => !!v || 'Confirme a senha',
      v => v === this.password || 'Senhas não coincidem',
    ],
  }),
  methods: {
    async register() {
      if (this.$refs.form.validate()) {
        try {
          // lembrar desse endpoint na hora do django
          const response = await axios.post('/api/register', {
            username: this.name,
            email: this.email,
            password: this.password
          });
        } catch(error){

        }
      }
    },
  },
};
</script>

<style>
.ajuste-btn{
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-evenly;
  width:100%;
  max-width: 100%;
}
</style>