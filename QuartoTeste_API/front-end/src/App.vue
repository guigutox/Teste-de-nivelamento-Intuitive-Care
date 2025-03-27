<template>
  <div class="container">
    <h1>Buscar Operadoras pelo DDD</h1>
    <div class="input-group">
      <input v-model="ddd" type="number" placeholder="Informe o DDD" />
      <button @click="buscarOperadoras">Buscar</button>
    </div>

    <div v-if="resultado.length" class="result-container">
      <h2>Resultados:</h2>
      <table class="result-table">
        <thead>
          <tr>
            <th>Razão Social</th>
            <th>Nome Fantasia</th>
            <th>CNPJ</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(operadora, index) in resultado" :key="index">
            <td>{{ operadora.Razao_Social }}</td>
            <td>{{ operadora.CNPJ }}</td>
            <td>{{ operadora.Logradouro }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p v-if="erro" class="erro">{{ erro }}</p>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const ddd = ref("");
    const resultado = ref([]);
    const erro = ref("");

    const buscarOperadoras = async () => {
      erro.value = "";
      resultado.value = [];

      if (!ddd.value) {
        erro.value = "Por favor, insira um DDD válido!";
        return;
      }

      try {
        const response = await fetch(`http://localhost:8000/buscar?ddd=${ddd.value}`);
        if (!response.ok) throw new Error("Erro ao buscar operadoras");
        resultado.value = await response.json();
      } catch (e) {
        erro.value = "Erro ao buscar operadoras. Tente novamente.";
      }
    };

    return { ddd, resultado, erro, buscarOperadoras };
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
  font-family: Arial, sans-serif;
}

.input-group {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

input {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.result-container {
  margin-top: 20px;
}

.result-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.result-table th,
.result-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.result-table th {
  background-color: #f4f4f4;
  font-weight: bold;
}

.erro {
  color: red;
  margin-top: 20px;
}
</style>