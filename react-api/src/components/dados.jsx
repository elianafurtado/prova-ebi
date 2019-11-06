import React from 'react'

const Dados = ({ dados }) => {
    return (
        <div>
            <center><h1>List</h1></center>
            <div className="card">
                <div className="card-body">
                    <h6 className="card-subtitle mb-2 text-muted">{dados.bairro}</h6>
                    {dados.atividades_secundarias.map(atividade =>
                        <div>
                            {atividade.code}
                            <p>{atividade.text}</p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
};

export default Dados