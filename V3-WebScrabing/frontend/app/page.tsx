"use client";
import { useState, useEffect } from 'react';
import { MdLightMode, MdDarkMode } from 'react-icons/md';

interface ScrapeResult {
  version: string;
  date: string;
  url: string;
}

export default function Home() {
  const [url, setUrl] = useState<string>("https://www.dbf2002.com/news.html");
  const [scrapedData, setScrapedData] = useState<ScrapeResult[] | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [theme, setTheme] = useState<'light' | 'dark'>('light'); // Default theme

  // Load theme from localStorage on initial render
  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') as 'light' | 'dark';
    if (savedTheme) {
      setTheme(savedTheme);
      document.documentElement.classList.add(savedTheme);
    } else {
      // Set default theme to light if nothing in localStorage
      document.documentElement.classList.add('light');
    }
  }, []);

  // Update theme in localStorage and on html element class when theme changes
  useEffect(() => {
    document.documentElement.classList.remove('light', 'dark');
    document.documentElement.classList.add(theme);
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  const handleScrape = async () => {
    setLoading(true);
    setError(null);
    setScrapedData(null);

    try {
      const response = await fetch(`http://localhost:8000/scrape?url=${encodeURIComponent(url)}`);
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      }
      const data: ScrapeResult[] = await response.json();
      setScrapedData(data);
    } catch (err: any) {
      setError(err.message || "An unknown error occurred.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900 p-8 text-gray-900 dark:text-gray-100 transition-colors duration-300">
      <div className="max-w-4xl mx-auto bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold text-gray-800 dark:text-gray-200">DBF Viewer 2000 Version Scraper</h1>
          <button
            onClick={toggleTheme}
            className="p-2 rounded-full bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors duration-300"
            aria-label="Toggle theme"
          >
            {theme === 'light' ? (
              <MdDarkMode className="h-6 w-6 text-gray-800" />
            ) : (
              <MdLightMode className="h-6 w-6 text-yellow-400" />
            )}
          </button>
        </div>

        <div className="flex flex-col md:flex-row gap-4 mb-8">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter website URL to scrape"
            className="flex-grow p-3 border border-gray-300 dark:border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100"
          />
          <button
            onClick={handleScrape}
            disabled={loading}
            className="bg-blue-600 text-white px-6 py-3 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? "Scraping..." : "Scrape Data"}
          </button>
        </div>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4" role="alert">
            <strong className="font-bold">Error:</strong>
            <span className="block sm:inline"> {error}</span>
          </div>
        )}

        {scrapedData && scrapedData.length > 0 && (
          <div className="overflow-x-auto">
            <table className="min-w-full bg-white dark:bg-gray-800 border-collapse">
              <thead>
                <tr className="bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-200 text-left">
                  <th className="py-3 px-4 border-b-2 border-gray-300 dark:border-gray-600">Version</th>
                  <th className="py-3 px-4 border-b-2 border-gray-300 dark:border-gray-600">Date</th>
                  <th className="py-3 px-4 border-b-2 border-gray-300 dark:border-gray-600">URL</th>
                </tr>
              </thead>
              <tbody>
                {scrapedData.map((item, index) => (
                  <tr key={index} className="border-b border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700">
                    <td className="py-3 px-4 text-black">{item.version}</td>
                    <td className="py-3 px-4 text-black">{item.date}</td>
                    <td className="py-3 px-4">
                      <a href={item.url} target="_blank" rel="noopener noreferrer" className="text-black hover:underline">
                        {item.url}
                      </a>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {scrapedData && scrapedData.length === 0 && !loading && !error && (
          <div className="bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-3 rounded relative" role="alert">
            <strong className="font-bold">No Data:</strong>
            <span className="block sm:inline"> No data was scraped for the provided URL.</span>
          </div>
        )}
      </div>
    </div>
  );
}
