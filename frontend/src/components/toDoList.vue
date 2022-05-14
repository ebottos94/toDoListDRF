<template>
<div v-if="isLoaded">
  <div class="container ">
      <div class="container ">
            <h3>Task rimanenti : {{ num_task }}</h3>
            <form @submit.prevent="addToList">
                <input type="text" class="form-control mt-3" placeholder="Aggiungi un nuovo task!" v-model="task" >
                <br>
                <div v-if="task_presenti">
                    <div  v-for="cosa in lista_cose" :key="cosa.idList" class="alert alert-success alert-dismissible fade show" role="alert">
                        {{ cosa.toDo }}
                        <button type="button" class="btn-close" aria-label="Close" v-on:click="elimina(cosa)"></button>
                    </div>
                </div>
                <p v-else>Per aggiungere un nuovo task, compila il campo testuale e premi invio.</p>
                
               
                  
                
            </form>
        </div>

      
  </div>
</div>
</template>

<script>
import { apiService } from "../common/api.service.js"
export default {
    name : "toDoList",

    data(){
        return{
            isLoaded : false,
            lista_cose : [],
            task : "",
            num_task : 0,
            task_presenti : false
        };
    },
    methods: {
        addToList() {
            let obj = {}
            if(this.lista_cose.length == 0){
                obj['toDo'] = this.task
                obj['idList'] = 0
            }
            else{
                obj['toDo'] = this.task
                obj['idList'] = this.lista_cose[this.lista_cose.length -1].idList +1
            }
            this.lista_cose.push(obj)
            this.task = ""
            this.num_task = this.lista_cose.length
            if(this.lista_cose.length>0){
                this.task_presenti = true
            }
            else{
                this.task_presenti = false
            }
            this.carica_Task(obj);
            
        },
        elimina(valore){
            this.lista_cose.splice(valore.idList, 1)
            for(let i=valore.idList; i<this.lista_cose.length;i++){
                this.lista_cose[i].idList=i;
            }
            this.num_task = this.lista_cose.length
            if(this.lista_cose.length>0){
                this.task_presenti = true
            }
            else{
                this.task_presenti = false
            }
            this.delete_Task(valore.id)
            for(let i=0; i<this.lista_cose.length;i++){
                this.update_Task(this.lista_cose[i]);
            }
        },
        get_Tasks() {
            let endpoint = "api/list/"
            apiService(endpoint)
            .then(data => {
                this.lista_cose = data
                if(this.lista_cose.length>0){
                    this.task_presenti = true
                }
                
                this.isLoaded = true
                console.log(this.lista_cose)
                this.num_task = this.lista_cose.length
            })
    },
    carica_Task(dati){
        let endpoint = "api/list/"
        let method = 'POST'
        apiService(endpoint, method, {content : dati})
        .then(data=>{
            console.log(data);
        })
    },
    update_Task(dati){
        let endpoint = "api/list/" + String(dati['id']) +'/'
        let method = 'PUT'
        apiService(endpoint, method, {content : dati})
        .then(data=>{
            console.log(data);
        })
    },
    delete_Task(id){
        let endpoint = "api/list/" + String(id) +'/'
        let method = 'DELETE'
        apiService(endpoint, method)
        .then(data=>{
            console.log(data);
        })
    }
            

    },
    created(){
        this.get_Tasks();
    }
    
}
</script>