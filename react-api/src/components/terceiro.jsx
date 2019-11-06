// import React, { Component } from 'react'
// import Template from './template'
// export default class Terceiro extends Component {
//     state = {
//         cnpj: "17895646000187",        
//         dados: []
//     }
//     constructor(props) {
//         super(props)        
//         this.setCnpj = this.setCnpj.bind(this)
//         // this.setDados = this.setDados.bind(this)
//         this.componentDidMount = this.componentDidMount.bind(this)
//     }  
//     setCnpj(e) {
//         this.setState({ cnpj: e.target.value })
//     }
//     // setDados(e){                        
//     //     fetch('https://www.receitaws.com.br/v1/cnpj/' + this.state.cnpj)
//     //         .then(res => res.json())
//     //         .then((data) => {
//     //             this.setState({ dados: data })
//     //         })
//     //         .catch(console.log)
//     // }
//     componentDidMount() {
//         fetch('https://www.receitaws.com.br/v1/cnpj/' + this.state.cnpj)
//             .then(res => res.json())
//             .then((data) => {
//                 this.setState({ dados: data })
//             })
//             .catch(console.log)
//         }
//     render() {
//         const { cnpj } = this.state
//         return (
//             <div className="container text-center">          
//                 <h1>Consultar CNPJ</h1>               
//                 <input type="text" placeholder="CNPJ" value={cnpj} onChange={this.setCnpj} />
//                 <button onClick={this.componentDidMount}>Buscar</button>
//                 <hr />
//                 <Template dados={this.state.dados}/>
//             </div>
//         )
//     }    
// }


