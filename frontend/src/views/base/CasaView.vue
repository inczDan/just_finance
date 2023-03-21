<template>
<div>
  <v-col cols="12" class="d-flex align-center justify-center">
    <v-img class="ajuste-img" contain height="240" src="@/assets/finance.png" />
  </v-col>
  <v-container class="ajuste-grafico fill-height align-start">
    <v-row>
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
      <v-col cols="10"> Aqui você pode visualizar os resumos das suas anotações. </v-col>
    </v-row>
    <div>
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-text>
          <v-form ref="form" method="post" id="form">
            <v-text-field v-model="nome" label="Nome" />
            <v-text-field v-model="valor_reais" label="Valor em reais" type="number" />
            <v-radio-group v-model="tipo" row>
              <v-radio label="Despesa" value="despesa" />
              <v-radio label="Receita" value="receita" />
            </v-radio-group>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-spacer />
          <v-btn color="blue darken-1" text @click="dialog = false">Cancelar</v-btn>
          <v-btn color="blue darken-1" text @click="createNote(), (dialog = false)"
            >Adicionar</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <div class="table-container py-4" color="blue">
      <table class="table">
        <thead>
          <tr>
            <th><v-checkbox v-model="selectedAll" @click="selectAll"></v-checkbox></th>
            <th>Nome</th>
            <th>Valor em reais</th>
            <th>Tipo</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="linha in linhas" :key="linha.nome">
            <td><v-checkbox v-model="linha.selected"></v-checkbox></td>
            <td>{{ linha.nome }}</td>
            <td>{{ linha.valor_reais }}</td>
            <td>{{ linha.tipo }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="d-flex justify-space-evenly align-self-end">
      <v-btn color="blue" :to="{ name: 'base-home' }">Voltar</v-btn>
      <v-btn color="blue" @click="dialog = true">Adicionar anotação</v-btn>
      <v-btn class="btn-apagar" color="red" @click="deleteSelected">Apagar selecionado</v-btn>
    </div>
  </div>
  </v-container>
</div>
</template>
<script>
import api from "@/api/tasks.api"
import accountsApi from "@/api/accounts.api"

export default {
  data: () => ({
    showProfile: false,
    showNovaAnotation: false,
    userName: "",
    dialog: false,
    selectAll: false,
    nome: "",
    valor_reais: "",
    tipo: "",
    linhas: [],
  }),
  mounted() {
    this.fetchNotes()
  },
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
    createNote() {
      if (this.$refs.form.validate()) {
        api
          .createNot(this.nome, this.valor_reais, this.tipo)
          .then((response) => {
            console.log(response.data)
            this.dialog = false
            this.fetchNotes()
            document.getElementById("form").reset();
          })
          .catch((error) => {
            console.error(error)
          })
      }
    },
    async fetchNotes() {
      const data = await api.getNotes()
      this.linhas = data.notes
    },
    async deleteSelected() {
      let selectedNotes = this.linhas.filter((linha) => linha.selected)
      if (selectedNotes.length > 0) {
        let deletedNotes = await api.deleteNotes(selectedNotes)
        console.log(deletedNotes.data)
        this.fetchNotes()
      }
    },
  },
  onMounted() {
    accountsApi.whoami().then((response) => {
      if (response.authenticated) {
        this.userName = response.user.username
      }
    })
  },
}
</script>

<script setup>
import { onMounted, ref } from "vue"
import axios from "axios"

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
.table-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.table {
  width: 100%;
  text-align: center;
  border-collapse: collapse;
  margin-top: 0px;
}
th,
td {
  padding: 0px;
  border: 1px solid #ddd;
}
th {
  background-color: rgb(25, 166, 242);
}
.btn-add {
  display: flex;
  justify-content: flex-end;
  width: 100%;
}
.btn-apagar {
  display: flex;
  justify-content: flex-end;
  width: 206px;
}
</style>
