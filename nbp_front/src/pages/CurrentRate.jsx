import React, { useState, useEffect } from "react";
import PropTypes from 'prop-types';

function CurrentRate({ setIsProcessing, currencyCode }) {

    const [currencies, setCurrencies] = useState([]);
    const [rates, setRates] = useState([]);

    const fetchData = async () => {
        var response = await fetch(
            'http://api.nbp.pl/api/exchangerates/rates/a/' + currencyCode.toLowerCase());

        if (!response.ok) {
            console.log("errorrr");
        }
        var data = await response.json();
        setCurrencies(data);
        setRates([data.rates[0].effectiveDate, data.rates[0].mid]);

        setIsProcessing = false;
    };

    useEffect(() => {
        setIsProcessing = true;
        fetchData();
    }, []);

    useEffect(() => {

    }, [rates]);

    return (
        <div>
            <h2>Exchange</h2>
            <div>Aktualny średni kurs waluty: {currencies.currency} [{currencies.code}]</div>
            <div>w dniu {rates[0]} to {rates[1]}PLN</div>
        </div>
    );
}

CurrentRate.propTypes = {
    setIsProcessing: PropTypes.func.isRequired,
};

export default CurrentRate;
