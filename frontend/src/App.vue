<template>
  <!-- <div>
    {{ usuario.username }}
  </div>
  <div>
    {{ usuario.name }}
  </div> -->
  <router-view />
</template>

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
