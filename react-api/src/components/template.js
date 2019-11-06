import React from 'react'

const Template = ({ dados }) => {
    return (
        <div>                        
            < div className="table-responsive" >
                <table class="table table-striped table-result">
                    <thead>
                        <tr>
                            <th colspan="4">Nome</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td colspan="4">{dados.nome}</td>
                        </tr>
                    </tbody>

                    <thead>
                        <tr>                            
                            <th colspan="1" class="ten wide">
                                Abertura</th>
                            <th colspan="1" class="six wide">
                                Email</th>
                            <th colspan="1" class="six wide">
                                Telefone</th>
                            <th colspan="1" class="two wide">
                                UF</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td colspan="1">{dados.abertura}</td>
                            <td colspan="1">{dados.email}</td>
                            <td colspan="1">{dados.telefone}</td>
                            <td colspan="1">{dados.uf}</td>
                            
                        </tr>
                    </tbody>
                    <thead>
                        <tr>
                            <th colspan="4">Atividade Principal</th>
                        </tr>
                        <tr>
                            <th colspan="1" class="two wide">
                                Código</th>
                            <th colspan="3">Descrição</th>
                        </tr>
                    </thead>
                    <tbody>
                                                                                
                            {
                                dados.atividade_principal.map(atividade =>
                                    <tr>
                                        <td colspan="1">{atividade.code}</td>
                                        <td colspan="3">{atividade.text}</td>
                                        <hr />
                                    </tr>
                                )
                            }
                        
                    </tbody>
                    <thead>
                        <tr>
                            <th colspan="4">Atividades Secundarias</th>
                        </tr>
                        <tr>
                            <th colspan="1" class="two wide">
                                Código</th>
                            <th colspan="3">Descrição</th>
                        </tr>
                    </thead>
                    <tbody>                        
                            {
                                dados.atividades_secundarias.map(atividade =>
                                    <tr>
                                        <td colspan="1">{atividade.code}</td>
                                        <td colspan="3">{atividade.text}</td>
                                        <hr />
                                    </tr>
                                )
                            }                        
                    </tbody>
                    
                </table>                                                                                                     
            </div >
        </div>
    )
};

export default Template    

