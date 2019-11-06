import React, { Component } from 'react'
import Template from './components/template'

export default class Terceiro extends Component {
    state = {
        cnpj: "",        
        dados: { atividades_secundarias: [], atividade_principal : []}
    }
    constructor(props) {
        super(props)        
        this.setCnpj = this.setCnpj.bind(this)              
        this.realizarConsulta = this.realizarConsulta.bind(this)              
    }  
    setCnpj(e) {
        this.setState({ cnpj: e.target.value })
    }    
    realizarConsulta() {
        const doc = this.state.cnpj
        const endpoint = 'https://www.receitaws.com.br/v1/cnpj/'
        fetch(endpoint+doc)
            .then(res => res.json())
            .then((data) => {
                this.setState({ dados: data })
            })
            .catch(console.log)
    }
    render() {
        const { cnpj } = this.state
        return (
            <div className="container text-center">          
                <h1>Consultar CNPJ</h1>               
                <input type="text" placeholder="CNPJ" value={cnpj} onChange={this.setCnpj} />
                <button className="btn btn-primary btn-sm" onClick={this.realizarConsulta}>Buscar</button>
                <hr />                
                <Template dados={this.state.dados}/>
            </div>
        )
    }    
}


