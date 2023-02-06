    <template>
        <v-container class="fill-height" >
        <v-row>
            <v-col cols="3" class="d-flex align-center justify-center">
                <v-menu offset-y v-model="showNovaAnotation">
                <template v-slot:activator="{ on }">
                    <v-btn class="options-btn" color="blue" @click="toggleAnotation">
                        <v-icon>mdi-plus-circle-outline</v-icon>
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item @click="addNote">
                        <v-list-item-title>Adicionar Nova Anotação</v-list-item-title>
                    </v-list-item>
                    <v-list-item @click="viewNotes">
                        <v-list-item-title>Visualizar Anotações</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
            </v-col>
            <v-col cols="6" class="d-flex align-center justify-center">
            <v-img contain height="240" src="@/assets/finance.png" />
            </v-col>
            <v-col cols="3" class="d-flex  justify-center">
            <v-hover>
                <v-btn class="profile-btn" @click="toggleProfile" color="blue">
                    <v-icon>mdi-account</v-icon>
                </v-btn>
            </v-hover>
            <v-expand-transition>
                <div v-if="showProfile">
                <v-card>
                    <v-card-title class="headline" >*Nome usuario*</v-card-title>
                    <v-list-item>
                    <v-btn
                    :to="{name: 'base-perfil'}"
                    @click="visuPerfil">
                    Perfil
                    </v-btn>
                    <br>
                    <v-btn
                    :to="{name: 'base-home'}"
                    @click="logout">
                        Deslogar
                    </v-btn>
                    </v-list-item>
                </v-card>
                </div>
            </v-expand-transition>
            </v-col>
        </v-row>
        <v-row class="mt-5">app1
            <v-col cols="12" class="d-flex align-center justify-center">
            Aqui você pode visualizar os resumos das suas anotações com gráficos.
            </v-col>
        </v-row>
        </v-container>
    </template>
    <script>
    import LoginView from '../accounts/LoginView.vue';

    export default {
        data: () => ({
        showProfile: false,
        showNovaAnotation: false,
        }),
        methods: {
            addNote() {
                //  direciona pra pagina de criar notações
                this.$router.push('tasks/novanota')
            },
            viewNotes() {
                // direciona p visualizar as anotações existentes
                this.$router.push('/tasks')
            },
            toggleProfile() {
                this.showProfile = !this.showProfile;
            },
            toggleAnotation(){
                this.showNovaAnotation = !this.showNovaAnotation;
            },
            logout() {
                // Remover o usuário da sessão
                // Redirecionar para a página de login
                this.$router.push('/logout')
            },
            visuPerfil(){
                this.$router.push('perfil')
            },
        },
    };
    </script>
    <style>
    .options-btn {
        position:absolute;
        top: 20px;
        left: 20px;
    }
    
    .profile-btn {
        position: absolute;
        top: 20px;
        right: 20px;
    }
    </style>