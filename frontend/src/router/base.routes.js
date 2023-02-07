// Composables
import EmptyLayout from "@/layouts/default/EmptyLayout.vue"
import HomeView from "@/views/base/HomeView.vue"
import GetStartedView from "@/views/base/GetStartedView.vue"
import CasaView from "@/views/base/CasaView.vue"
import PerfilView from "@/views/base/PerfilView.vue"

export default [
  {
    path: "/",
    component: EmptyLayout,
    children: [
      {
        path: "",
        name: "base-home",
        component: HomeView,
      },
      {
        path: "getstarted",
        name: "base-getstarted",
        component: GetStartedView,
      },
      {
        path: "casinha",
        name: "base-casinha",
        component: CasaView,
      },
      {
        path: "profile",
        name: "base-perfil",
        component: PerfilView,
      }
    ],
  },
]
