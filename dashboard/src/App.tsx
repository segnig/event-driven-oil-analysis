import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DatePicker from 'react-datepicker';
import "react-datepicker/dist/react-datepicker.css";
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ReferenceArea, ReferenceLine, ResponsiveContainer
} from 'recharts';
import './App.css';

// --- (Keep your interfaces) ---
interface PriceDataPoint {
  Date: string;
  Price: number | null;
  Log_Return: number | null;
}
interface EventData {
  EventDate: string;
  Description: string;
}
interface ChangepointData {
  startDate: string;
  endDate: string;
  description: string;
  impact: { metric: string; value: string; };
}

const API_URL = 'http://127.0.0.1:5000';

function App(): React.ReactElement {
  const [priceData, setPriceData] = useState<PriceDataPoint[]>([]);
  const [events, setEvents] = useState<EventData[]>([]);
  const [changepoint, setChangepoint] = useState<ChangepointData | null>(null);
  const [startDate, setStartDate] = useState<Date | null>(new Date('2005-01-01'));
  const [endDate, setEndDate] = useState<Date | null>(new Date('2010-12-31'));
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Do not fetch data if the date range is incomplete
    if (!startDate || !endDate) {
      return;
    }

    const fetchData = async () => {
      setLoading(true);
      setError(null);

      const start = startDate.toISOString().split('T')[0];
      const end = endDate.toISOString().split('T')[0];

      try {
        const [priceRes, eventsRes, changepointRes] = await Promise.all([
          axios.get<PriceDataPoint[]>(`${API_URL}/api/price-data`, { params: { start, end } }),
          axios.get<EventData[]>(`${API_URL}/api/events`),
          axios.get<ChangepointData>(`${API_URL}/api/changepoint`)
        ]);

        if (Array.isArray(priceRes.data)) {
          setPriceData(priceRes.data);
        } else {
          setError("Failed to load price data in the correct format.");
        }
        
        setEvents(eventsRes.data);
        setChangepoint(changepointRes.data);

      } catch (err) {
        setError("Could not connect to the data server.");
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, [startDate, endDate]);

  const relevantEvents = events.filter(event => 
    new Date(event.EventDate) >= (startDate || new Date('1900-01-01')) && 
    new Date(event.EventDate) <= (endDate || new Date('2100-01-01'))
  );

  return (
    <div className="App">
      <header className="App-header">
        <h1>Brent Oil Price Analysis Dashboard</h1>
      </header>
      <main>
        <div className="filter-container">
          <div>
            <label>Start Date:</label>
            <DatePicker selected={startDate} onChange={(date: Date | null) => setStartDate(date)} />
          </div>
          <div>
            <label>End Date:</label>
            <DatePicker selected={endDate} onChange={(date: Date | null) => setEndDate(date)} />
          </div>
        </div>

        <div className="chart-container">
          <h2>Price Volatility and Key Events</h2>
          {loading ? (
             <div>Loading chart data...</div>
          ) : error ? (
            <div className="error-message">{error}</div>
          ) : (
            <ResponsiveContainer width="95%" height={500}>
              {/* --- COMPLETE CHART CODE --- */}
              <LineChart
                data={priceData}
                margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="Date" tick={{ fontSize: 12 }} />
                <YAxis yAxisId="left" label={{ value: 'Price ($)', angle: -90, position: 'insideLeft' }} />
                <YAxis yAxisId="right" orientation="right" label={{ value: 'Log Return', angle: 90, position: 'insideRight' }} />
                <Tooltip />
                <Legend />

                <Line yAxisId="left" type="monotone" dataKey="Price" stroke="#8884d8" dot={false} name="Price" />
                <Line yAxisId="right" type="monotone" dataKey="Log_Return" stroke="#82ca9d" dot={false} strokeOpacity={0.5} name="Volatility" />

                {changepoint && (
                  <ReferenceArea
                    yAxisId="left"
                    x1={changepoint.startDate}
                    x2={changepoint.endDate}
                    stroke="red"
                    strokeOpacity={0.3}
                    fill="red"
                    fillOpacity={0.1}
                    label={{
                      value: changepoint.description,
                      position: "insideTop",
                      fill: "#d00",
                      fontSize: 14,
                    }}
                  />
                )}

                {relevantEvents.map((event) => (
                  <ReferenceLine
                    key={event.Description}
                    yAxisId="left"
                    x={event.EventDate}
                    stroke="green"
                    strokeDasharray="3 3"
                    label={{
                      value: event.Description,
                      angle: -90,
                      position: 'insideBottomLeft',
                      fill: '#333',
                      fontSize: 10,
                    }}
                  />
                ))}
              </LineChart>
            </ResponsiveContainer>
          )}
        </div>
        
        <div className="summary-card">
            <h3>Key Finding</h3>
            {changepoint && (
                <p>
                    A <strong>{changepoint.impact.metric}</strong> of <strong>{changepoint.impact.value}</strong> 
                    was detected during the transition period from {changepoint.startDate} to {changepoint.endDate}, 
                    coinciding with the build-up to the 2008 Global Financial Crisis.
                </p>
            )}
        </div>
      </main>
    </div>
  );
}

export default App;