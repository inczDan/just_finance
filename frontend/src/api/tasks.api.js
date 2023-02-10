import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
  getNotes: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/tasks/mostra")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },

  addNewTask: (description) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/tasks/add", apiHelpers.dataToForm({ description }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  createNot: (nome, valor_reais, tipo, user) => {
    return api
      .post("/api/tasks/save", {
        nome: nome,
        valor_reais: valor_reais,
        tipo: tipo,
        user: user,
      })
      .then((response) => {
        return response.data
      })
      .catch((error) => {
        return error
      })
  },
  // createNot: (nome, valor_reais, tipo) => {
  //   return api
  //     .post("/api/tasks/save", apiHelpers.dataToForm({ nome, valor_reais, tipo }))
  //     .then((response) => {
  //       return response.data
  //     })
  //     .catch((error) => {
  //       return error
  //     })
  // },
}
