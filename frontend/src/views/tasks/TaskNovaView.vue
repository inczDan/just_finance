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
        <v-text-field
          label="Nome"
          v-model="nome"
        />
        <v-text-field
          label="Valor em reais"
          v-model="valor"
          type="number"
        />
        <v-radio-group v-model="tipo" row>
          <v-radio
            label="Despesa"
            value="despesa"
          />
          <v-radio
            label="Receita"
            value="receita"
          />
        </v-radio-group>
      </v-form>
    </v-card-text>

    <v-card-actions>
      <v-spacer />
      <v-btn color="blue darken-1" text @click="dialog = false">Cancelar</v-btn>
      <v-btn color="blue darken-1" text @click="addLinha">Adicionar</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>
<div class="table-container" color="blue">
    <!-- Tabela com as linhas adicionadas -->
    <table class="table" >
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
          <td>{{ linha.valor }}</td>
          <td>{{ linha.tipo }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  </div>
  <div class='ajusta-btn'>
  <v-btn  color="blue" @click="dialog = true">Adicionar anotação</v-btn>
    <v-btn class='btn-apagar' color="red" @click="deleteSelected">Apagar selecionados</v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      selectAll:false,
      nome: '',
      valor: '',
      tipo:'',
      linhas: []
    };
  },
  methods: {
    addLinha() {
      // Verifica se o formulário é válido
      if (this.$refs.form.validate()) {
        // Adiciona a nova linha à lista de linhas
        this.linhas.push({
          nome: this.nome,
          valor: this.valor,
          tipo: this.tipo,
        })
        // Limpa os campos do formulário
        this.nome = ''
        this.valor = ''
        this.tipo = ''

        // Fecha a janela modal
        this.dialog = false
      }
    }
  }
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
  th, td {
    padding: 0px;
    border: 1px solid #ddd;
  }
  th {
    background-color: rgb(25, 166, 242);
  }
  .btn-add{
    display:flex;
    justify-content: flex-end;
    width: 100%;
  }
  .btn-apagar{
    display: flex;
    justify-content: flex-end;
    width: 206px;
  }
  .ajusta-btn {
    display:flex;
    align-items:flex-end;
    justify-content:space-around;
    position: fixed;
    bottom: 10%;
    left:34%;
    padding:0.5%;
  }
</style>