<template>
  <div>
    <!-- Botão para abrir a janela modal -->
    <!-- <div class="btn-add">
      
    </div> -->
    <!-- Janela modal -->
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <!-- Formulário para inserir o nome, o valor em reais e se é uma despesa ou receita -->
        <v-card-text>
          <v-form ref="form">
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
    <div class="table-container" color="blue">
      <!-- Tabela com as linhas adicionadas -->
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
  </div>
  <div class="ajusta-btn">
    <v-btn color="blue" :to="{ name: 'base-casinha' }">Voltar</v-btn>
    <v-btn color="blue" @click="dialog = true">Adicionar anotação</v-btn>
    <v-btn class="btn-apagar" color="red" @click="deleteSelected">Apagar selecionado</v-btn>
  </div>
</template>
<script>
import api from "@/api/tasks.api"

export default {
  data() {
    return {
      dialog: false,
      selectAll: false,
      nome: "",
      valor_reais: "",
      tipo: "",
      linhas: [],
    }
  },
  mounted() {
    this.fetchNotes()
  },
  methods: {
    createNote() {
      if (this.$refs.form.validate()) {
        api
          .createNot(this.nome, this.valor_reais, this.tipo)
          .then((response) => {
            console.log(response.data)
            this.dialog = false
            this.fetchNotes()
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
}
</script>
<style>
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
.ajusta-btn {
  display: flex;
  width: 70%;
  align-items: flex-end;
  justify-content: space-evenly;
  position: fixed;
  bottom: 10%;
  left: 15%;
  padding: 0.5%;
}
</style>
