// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import TaskListView from "@/views/tasks/TaskListView.vue"
import TaskNovaView from "@/views/tasks/TaskNovaView.vue"

export default [
  {
    path: "/tasks",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "tasks-list",
        component: TaskListView,
      },
      {
        path: "novanotacao",
        name: "tasks-nova",
        component: TaskNovaView,
      }
    ],
  },
]
