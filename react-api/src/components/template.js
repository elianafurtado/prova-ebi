import React from 'react'

const Template = ({ dados }) => {
    return (
        <div>
            <center><h1>Informações sobre o CNPJ</h1></center>            
            < div className="table-responsive" >
                    <h5 className="card-title">{dados.nome}</h5>
                    <h5 className="card-title">{dados.uf}</h5>
                    <h5 className="card-title">{dados.telefone}</h5>
                    <h5 className="card-title">{dados.email}</h5>
                    <h5 className="card-title">{dados.abertura}</h5>                
                                       
            </div >
        </div>
    )
};

export default Template    

// {
//     dados.atividade_principal.map(atividade =>
//         <div>
//             <p>{atividade.text}</p>
//             <hr />
//         </div>
//     )
// }
// {
//     dados.atividades_secundarias.map(atividade =>
//         <div>
//             <p>{atividade.text}</p>
//             <hr />
//         </div>
//     )
// }