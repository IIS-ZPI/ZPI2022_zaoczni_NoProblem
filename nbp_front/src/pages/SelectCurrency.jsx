import React, { useState, useEffect } from "react";
import PropTypes from 'prop-types';

function SelectCurrency({ setIsProcessing }) {
    const [currenciesList, setCurrenciesList] = useState([]);
    const [myResponseData, setMyResponseData] = useState(null);

    const fetchData = async () => {
        const response = await fetch('http://api.nbp.pl/api/exchangerates/tables/a/');
        if (!response.ok) {
            console.log("errorrr");
        }

        const data = await response.json();
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
            <div>Lista walut</div>
            {currenciesList.map((curr, index) => (<div key={index}>{curr[0]} - {curr[1]}</div>))}
        </div>
    );
}

SelectCurrency.propTypes = {
    setIsProcessing: PropTypes.func.isRequired,
};

export default SelectCurrency;
