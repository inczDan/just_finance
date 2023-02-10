import api from "./config.js"
import apiHelpers from "./helpers.js"
import axios from "axios"

const updateProfilePicture = (picture) => {
  if (!picture) {
    throw new Error("A imagem do perfil não foi definida")
  }
  return axios.patch("/api/accounts/profile/", { picture }).then((response) => response.data)
}

export default {
  updateProfilePicture,
  whoami: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/accounts/whoami")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  login: (username, password) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/accounts/login", apiHelpers.dataToForm({ username, password }))
        .then((response) => {
          if (response.status === 200) {
            return resolve(response.data)
          } else {
            return reject(new Error("Autenticação falhou"))
          }
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  logout: () => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/accounts/logout")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  getregister: (username, email, password) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/accounts/getstarted", {
          username: username,
          email: email,
          password: password,
        })
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
}
