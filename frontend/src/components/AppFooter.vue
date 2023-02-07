<template>
  <v-footer :absolute="!fixed" app>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" lg="6" md="6" align-self="center" class="pa-0">
          <div class="px-5 text-grey text-center">
            <span v-if="user" class="pl-4">
              <v-icon>mdi-account</v-icon>
              {{ user.username }}
            </span>
            <v-col cols="12" align-self="center" class="pa-0 text-center">
          <span> &copy; {{ new Date().getFullYear() }} - Just Finance </span>
        </v-col>
          <a 
            href="https://api.whatsapp.com/send?phone=5511946534685&text=Preciso%20de%20suporte%20com%20o%20Just%20Finance%20por%20favor"
            target="_blank">
            <span class="px-5">Entre em contato</span>
          </a>
          </div>
        </v-col>
       
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  props: {
    fixed: {
      type: Boolean,
      default: true,
    },
    user: {
      type: Object,
      default: null,
    },
  },
  data: () => ({
    apiBaseUrl: import.meta.env.VITE_API_BASE_URL,
    nodeEnv: import.meta.env.VITE_NODE_ENV,
  }),
}
</script>
