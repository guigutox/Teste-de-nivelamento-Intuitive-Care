<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <div class="input-group">
      <input v-model="termo_busca" type="text" placeholder="Informe o termo de busca (nome, CNPJ ou endereço)" />
      <button @click="buscarOperadoras">Buscar</button>
    </div>

    <div v-if="resultado.length" class="result-container">
      <h2>Resultados:</h2>
      <div class="table-wrapper">
        <table class="result-table">
          <thead>
            <tr>
              <th>Registro ANS</th>
              <th>Razão Social</th>
              <th>Nome Fantasia</th>
              <th>CNPJ</th>
              <th>Endereço</th>
              <th>Modalidade</th>
              <th>Número</th>
              <th>Complemento</th>
              <th>Bairro</th>
              <th>Cidade</th>
              <th>UF</th>
              <th>CEP</th>
              <th>Telefone</th>
              <th>E-mail</th>
              <th>Representante</th>
              <th>Cargo Representante</th>
              <th>Regiao de Comerializacao</th>
              <th>Data Registro ANS</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(operadora, index) in resultado" :key="index">
              <td>{{ operadora.Registro_ANS }}</td>
              <td>{{ operadora.Razao_Social }}</td>
              <td>{{ operadora.Nome_Fantasia }}</td>
              <td>{{ operadora.CNPJ }}</td>
              <td>{{ operadora.Logradouro }}</td>
              <td>{{ operadora.Modalidade }}</td>
              <td>{{ operadora.Numero }}</td>
              <td>{{ operadora.Complemento }}</td>
              <td>{{ operadora.Bairro }}</td>
              <td>{{ operadora.Cidade }}</td>
              <td>{{ operadora.UF }}</td>
              <td>{{ operadora.CEP }}</td>
              <td>{{ operadora.Telefone }}</td>
              <td>{{ operadora.Endereco_eletronico }}</td>
              <td>{{ operadora.Representante }}</td>
              <td>{{ operadora.Cargo_Representante }}</td>
              <td>{{ operadora.Regiao_de_Comercializacao }}</td>
              <td>{{ operadora.Data_Registro_ANS }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <p v-if="erro" class="erro">{{ erro }}</p>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const termo_busca = ref("");
    const resultado = ref([]);
    const erro = ref("");
    
    const buscarOperadoras = async () => {
      erro.value = "";
      resultado.value = [];
      
      if (!termo_busca.value) {
        erro.value = "Por favor, insira um termo de busca válido!";
        return;
      }

      try {
        const response = await fetch(`http://localhost:8000/buscar?termo_busca=${encodeURIComponent(termo_busca.value)}`);
        if (!response.ok) throw new Error("Erro ao buscar operadoras");
        resultado.value = await response.json();
      } catch (e) {
        erro.value = "Erro ao buscar operadoras. Tente novamente.";
        console.error(e);
      }
    };

    return { termo_busca, resultado, erro, buscarOperadoras };
  },
};
</script>

<style scoped>

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.container {
  max-width: 95%;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: rgb(255, 255, 255);
}

.input-group {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
  gap: 10px;
}

input {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  min-width: 300px;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #0051ff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  white-space: nowrap;
}

button:hover {
  background-color: #0056b3;
}

.result-container {
  margin-top: 20px;
  width: 100%;
  overflow-x: auto;
}

.table-wrapper {
  width: 100%;
  overflow-x: auto;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  border-radius: 8px;
}

.result-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  min-width: 1200px; /* Largura mínima para manter as colunas legíveis */
}

.result-table th,
.result-table td {
  border: 1px solid #ddd;
  padding: 8px 12px;
  text-align: left;
  white-space: nowrap;
}

.result-table th {
  background-color: #cac8c8;
  font-weight: bold;
  position: sticky;
  top: 0;
}

.result-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.result-table tr:hover {
  background-color: #f1f1f1;
}

.erro {
  color: red;
  margin-top: 20px;
  text-align: center;
}

@media (max-width: 768px) {
  .input-group {
    flex-direction: column;
    align-items: center;
  }
  
  input {
    width: 100%;
    margin-right: 0;
    margin-bottom: 10px;
  }
}
</style>