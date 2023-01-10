import React, { useState, useEffect } from "react";
import Select from "react-select";
import PropTypes from 'prop-types';

function SelectCurrency({ setIsProcessing, onQuery }) {
    const [currenciesList, setCurrenciesList] = useState([]);
    const [myResponseData, setMyResponseData] = useState(null);
    const [selectedValue, SetSelectedValue] = useState("");

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
            });
            setCurrenciesList(currencies);
        }
    }, [myResponseData]);

    function handleInput(e) {
        onQuery(e.value);
    }

    return (
        <div>
            <div>Lista walut</div>
            <Select
                onChange={handleInput}
                className="select-currency"
                placeholder="Wybierz walutę..."
                options={currenciesList.map((curr) => ({ value: curr[1], label: curr[0] + ' - ' + curr[1] }))}
            />
            <div>{selectedValue}</div>
        </div>
    );
}

SelectCurrency.propTypes = {
    setIsProcessing: PropTypes.func.isRequired,
    currenciesList: PropTypes.array,
};

export default SelectCurrency;
