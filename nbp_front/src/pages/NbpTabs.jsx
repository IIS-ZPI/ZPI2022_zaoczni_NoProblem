import React, { useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import Alert from 'react-bootstrap/Alert';

import CurrentRate from "./CurrentRate";
import SelectCurrency from "./SelectCurrency";

function NbpTabs({ setIsProcessing }) {

    const [query, setQuery] = useState(null);

    return (
        <>
            <Tabs id="NbpTabs" className='mb-3' justify>
                <Tab eventKey="tab1" title="Analiza waluty">
                    <SelectCurrency setIsProcessing={true} onQuery={setQuery} />
                    <CurrentRate setIsProcessing={true} query={query} />
                </Tab>

                <Tab eventKey="tab2" title="Zestawienie">
                    <Alert variant="info">Placeholder for Tab2</Alert>
                </Tab>
            </Tabs>
        </>
    )
}

export default NbpTabs;
