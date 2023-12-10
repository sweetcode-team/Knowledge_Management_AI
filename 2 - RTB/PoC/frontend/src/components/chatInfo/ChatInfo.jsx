import React from 'react'
import './chatInfo.css'

export default function ChatInfo({ }){

    return (
        <div className="main__chatlist">
            <div className="chatlist__heading">
                <h3>About</h3>
            </div>

            <div className='about__section'>
                <p>
                    Un sistema di <strong>Knowledge Management AI</strong> è un potente strumento progettato per ottimizzare la gestione delle informazioni in un'organizzazione.
                    <br />
                    <br />
                    Questo servizio offre un modo efficiente e intuitivo per centralizzare, organizzare e accedere alle risorse aziendali.
                    <br />
                    <br />
                    Carica dei documenti e inizia a chattare!
                </p>
            </div>
        </div>
    )
}
