<template>
  <div class="row">
    <div class="col-8">
  <q-form @submit.prevent="submitForm">
    <div
      v-for="(row, index) in formRows"
      :key="index"
      class="row"
    >
      <q-input
        square outlined
        v-model="row.num_formule"
        color="cyan-4"
        class="col-1"
      />
      <q-select
        square outlined
        v-model="row.parametre"
        color="cyan-4"
        class="col-6 hover-effect"
        :options="allParametresLabel"
        option-label="label"
        option-value="id"
      />
      <q-btn-group flat class="q-ml-lg">
        <q-btn flat size="sm" @click="addRow" icon="check_circle" color="cyan-4" class="hover-effect-success"/>
        <q-btn flat size="sm" @click="removeRow" icon="delete_forever" color="cyan-4" class="hover-effect-warning"/>
      </q-btn-group>
    </div>

    <div class="row">
      <div class="col-4">
        <q-btn flat @click="submitForm" color="green-4" class="q-mt-xs">
          Valider
        </q-btn>
      </div>
    </div>
  </q-form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import api from "../../../api";

export default {
  data() {
    return {
      selectedRowIndex: null,
      formRows: [
        {
          num_formule: null,
          parametre: null,
        }
      ],
    };
  },
  computed: {
    ...mapGetters('formules', ['allParametres']),
    allParametresLabel() {
      // Calculer le libellé complet avec le nom et le fournisseur
      return this.allParametres.map(parametre => ({
        ...parametre,
        label: `${parametre.nom} - ${parametre.unite}`,
      }));
    },
  },

  async created() {
      this.loadLastId();
      this.loadParametres();

    },

  methods: {
    ...mapActions('formules', ['loadParametres', 'addParametre']),

    async loadLastId() {
      try {
        // Utilisez une API Django ou Axios pour récupérer le dernier ID + 1
        const response = await api.get('/PPH/nouvelle-formule/dernier_id');
        const dernierId = response.data.dernierId;

        // Incrémentez l'ID de 1 pour obtenir la nouvelle valeur de num_formule
        const newNumFormule = dernierId + 1;

        // Initialisez la première ligne du formulaire avec le dernier ID + 1
        this.formRows[0].num_formule = newNumFormule;
      } catch (error) {
        console.error('Erreur lors de la récupération du dernier ID de la formule', error);
      }
    },

    async addRow() {
      // Récupérez l'ID du dernier enregistrement du modèle Formule depuis votre API Django
      try {
        const response = await api.get('PPH/nouvelle-formule/dernier_id/');
        const dernierId = response.data.dernierId;

        // Incrémentez l'ID de 1 pour obtenir la nouvelle valeur de num_formule
        const newNumFormule = dernierId + 1;

        // Ajoutez une nouvelle ligne au tableau formRows avec le nouveau num_formule
        this.formRows.push({
          num_formule: newNumFormule,
          parametre: null,
        });
      } catch (error) {
        console.error('Erreur lors de la récupération du dernier ID du modèle Formule', error);
      }
    },

    removeRow(row) {
      // Supprime la ligne qui contient le bouton
      const index = this.formRows.indexOf(row);
      this.formRows.splice(index, 1);
    },

    async submitForm() {
      // Récupérez les données de toutes les lignes
      const formData = {
        parametres: this.formRows.map(row => ({
          num_formule: row.num_formule,
          parametre: row.parametre,
        })),
      };

      // Appelez votre action Vuex pour ajouter les compositions
      this.addParametre(formData);
    },
  },
};
</script>


