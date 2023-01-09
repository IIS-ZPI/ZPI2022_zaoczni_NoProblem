import React, { useState, useEffect } from "react";
import PropTypes from 'prop-types';

function Exchange({ setIsProcessing }) {

    const [currencies, setCurrencies] = useState([]);
    const [rates, setRates] = useState([]);

    const [currenciesList, setCurrenciesList] = useState([]);
    const [myResponseData, setMyResponseData] = useState(null);

    const fetchData = async () => {
        var response = await fetch(
            'http://api.nbp.pl/api/exchangerates/rates/a/usd');
        if (!response.ok) {
            console.log("errorrr");
        }
        var data = await response.json();
        setCurrencies(data);
        setRates([data.rates[0].effectiveDate, data.rates[0].mid]);

        response = await fetch('http://api.nbp.pl/api/exchangerates/tables/a/');
        if (!response.ok) {
            console.log("errorrr");
        }

        data = await response.json();
        setMyResponseData(data);
        setIsProcessing = false;
    };

    useEffect(() => {
        setIsProcessing = true;
        fetchData();
    }, []);

    useEffect(() => {
        if (myResponseData) {
            let currencies = [];
            myResponseData[0].rates.forEach(function (d) {
                currencies.push([d.currency, d.code]);
                console.log(d.currency, d.code);
            });
            setCurrenciesList(currencies);
        }
    }, [myResponseData]);

    return (
        <div>
            <h2>Exchange</h2>
            <div>Aktualny średni kurs waluty: {currencies.currency} [{currencies.code}]</div>
            <div>w dniu {rates[0]} to {rates[1]}PLN</div>

            <br /><div>Lista walut</div>
            {currenciesList.map((curr, index) => (<div key={index}>{curr[0]} - {curr[1]}</div>))}
        </div>
    );
}

Exchange.propTypes = {
    setIsProcessing: PropTypes.func.isRequired,
};

export default Exchange;
