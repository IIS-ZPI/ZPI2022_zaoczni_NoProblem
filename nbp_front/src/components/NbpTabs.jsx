import React, { useState } from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import Alert from 'react-bootstrap/Alert';

import CurrentRate from "./../pages/CurrentRate";
import SelectCurrency from "./../pages/SelectCurrency";

function NbpTabs({ setIsProcessing }) {


    return (
        <>
            <Tabs id="NbpTabs" className='mb-3' justify>
                <Tab eventKey="tab1" title="Analiza waluty">
                    <CurrentRate setIsProcessing={true} currencyCode="USD" />
                    <SelectCurrency setIsProcessing={true} />
                </Tab>
                <Tab eventKey="tab2" title="Zestawienie">
                    <Alert variant="info">Placeholder for Tab2</Alert>
                </Tab>

            </Tabs>
        </>
    )
}

export default NbpTabs;
