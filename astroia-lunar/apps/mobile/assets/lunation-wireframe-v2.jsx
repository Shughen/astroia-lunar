import React, { useState } from 'react';

const LunationWireframe = () => {
  const [activeTab, setActiveTab] = useState('cycle');
  const [showBottomSheet, setShowBottomSheet] = useState(false);
  const [sheetHeight, setSheetHeight] = useState('peek');

  const toggleSheet = () => {
    if (!showBottomSheet) {
      setShowBottomSheet(true);
      setSheetHeight('half');
    } else if (sheetHeight === 'half') {
      setSheetHeight('full');
    } else {
      setShowBottomSheet(false);
      setSheetHeight('peek');
    }
  };

  const closeSheet = () => {
    setShowBottomSheet(false);
    setSheetHeight('peek');
  };

  // VoC Status - simulated
  const vocActive = true;
  const vocEndTime = "14:32";

  return (
    <div className="relative w-full max-w-sm mx-auto h-[750px] bg-gradient-to-b from-purple-950 via-purple-900 to-purple-950 rounded-3xl overflow-hidden shadow-2xl border border-purple-800/30">
      
      {/* Status Bar */}
      <div className="flex justify-between items-center px-6 py-2 text-white text-sm">
        <span>4:14</span>
        <div className="w-6 h-6 bg-black rounded-full"></div>
        <div className="flex gap-1">
          <span>📶</span>
          <span>🔋</span>
        </div>
      </div>

      {/* Main Content Area */}
      <div className="h-[620px] overflow-y-auto">
        
        {/* Tab: Mon Cycle */}
        {activeTab === 'cycle' && (
          <div className="flex flex-col px-4 pt-2 pb-4">
            {/* Header */}
            <div className="text-center mb-4">
              <h1 className="text-2xl font-bold text-white tracking-wide">Lunation</h1>
              <p className="text-purple-300 text-sm">Ton rituel lunaire</p>
            </div>

            {/* VoC Alert Banner - si actif */}
            {vocActive && (
              <div className="mb-3 bg-gradient-to-r from-amber-600/30 to-orange-600/30 rounded-xl p-3 border border-amber-500/40 flex items-center gap-3">
                <div className="w-8 h-8 rounded-full bg-amber-500/30 flex items-center justify-center">
                  <span className="text-amber-300">⚠️</span>
                </div>
                <div className="flex-1">
                  <p className="text-amber-200 text-sm font-medium">Void of Course actif</p>
                  <p className="text-amber-300/70 text-xs">Jusqu'à {vocEndTime} • Évite les décisions majeures</p>
                </div>
                <button className="text-amber-300 text-xs underline">Info</button>
              </div>
            )}

            {/* Hero Card - Révolution Lunaire */}
            <div className="bg-gradient-to-br from-purple-800/60 to-purple-900/80 rounded-3xl p-6 border border-purple-500/30 backdrop-blur relative overflow-hidden">
              {/* Decorative elements */}
              <div className="absolute top-4 right-4 w-20 h-20 bg-purple-400/10 rounded-full blur-xl"></div>
              <div className="absolute bottom-20 left-4 w-16 h-16 bg-yellow-400/10 rounded-full blur-xl"></div>
              
              {/* Moon phase indicator */}
              <div className="absolute top-4 right-4 flex flex-col items-center">
                <div className="w-12 h-12 rounded-full bg-gradient-to-r from-yellow-100 to-yellow-200 shadow-lg shadow-yellow-400/30"></div>
              </div>

              <p className="text-purple-300 text-sm uppercase tracking-widest mb-2">Mon cycle actuel</p>
              
              <h2 className="text-4xl font-bold text-white mb-1">Janvier 2026</h2>
              <p className="text-purple-300 mb-6">15 janv. - 13 févr.</p>

              <div className="h-px bg-purple-500/30 my-4"></div>

              {/* Lunar positions */}
              <div className="flex gap-8 mb-6">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-red-500/20 flex items-center justify-center">
                    <span className="text-red-400 text-lg">♐</span>
                  </div>
                  <div>
                    <p className="text-purple-400 text-xs uppercase">Lune en</p>
                    <p className="text-white font-semibold">Sagittaire</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-purple-500/20 flex items-center justify-center">
                    <span className="text-purple-300 text-lg">♍</span>
                  </div>
                  <div>
                    <p className="text-purple-400 text-xs uppercase">Ascendant</p>
                    <p className="text-white font-semibold">Vierge</p>
                  </div>
                </div>
              </div>

              {/* Thèmes du mois */}
              <div className="mb-6">
                <p className="text-purple-400 text-xs uppercase mb-2">Thèmes du mois</p>
                <div className="flex flex-wrap gap-2">
                  <span className="px-3 py-1 bg-purple-600/40 rounded-full text-purple-200 text-sm">Expansion</span>
                  <span className="px-3 py-1 bg-purple-600/40 rounded-full text-purple-200 text-sm">Organisation</span>
                  <span className="px-3 py-1 bg-purple-600/40 rounded-full text-purple-200 text-sm">Détails</span>
                </div>
              </div>

              {/* CTA Button */}
              <button className="w-full py-3 bg-gradient-to-r from-purple-500 to-purple-600 rounded-xl text-white font-semibold flex items-center justify-center gap-2 hover:from-purple-400 hover:to-purple-500 transition-all shadow-lg shadow-purple-500/30">
                <span>Voir le rapport mensuel</span>
                <span>→</span>
              </button>
            </div>

            {/* Mini card "Aujourd'hui" - Clickable */}
            <button 
              onClick={toggleSheet}
              className="mt-4 bg-purple-800/50 rounded-2xl p-4 border border-purple-500/20 flex items-center justify-between hover:bg-purple-800/70 transition-all"
            >
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-gradient-to-r from-yellow-100 to-yellow-50 flex items-center justify-center shadow-md">
                  <span className="text-yellow-600">🌓</span>
                </div>
                <div className="text-left">
                  <p className="text-purple-300 text-xs">Aujourd'hui</p>
                  <p className="text-white font-medium">Lune Gibbeuse en Gémeaux</p>
                </div>
              </div>
              <div className="text-purple-400">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 15l7-7 7 7" />
                </svg>
              </div>
            </button>

            {/* Mini card "Thème Natal" - Raccourci */}
            <button 
              onClick={() => setActiveTab('profile')}
              className="mt-3 bg-purple-800/30 rounded-2xl p-4 border border-purple-500/10 flex items-center justify-between hover:bg-purple-800/50 transition-all"
            >
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-full bg-purple-600/30 flex items-center justify-center">
                  <span className="text-purple-300">⊛</span>
                </div>
                <div className="text-left">
                  <p className="text-white font-medium">Mon thème natal</p>
                  <p className="text-purple-400 text-xs">Découvre ton ciel de naissance</p>
                </div>
              </div>
              <div className="text-purple-500">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </div>
            </button>
          </div>
        )}

        {/* Tab: Calendrier */}
        {activeTab === 'calendar' && (
          <div className="h-full px-4 pt-2">
            <h1 className="text-2xl font-bold text-white text-center mb-6">Calendrier Lunaire</h1>
            
            <div className="flex items-center justify-between mb-4">
              <button className="text-purple-400 text-xl">‹</button>
              <h2 className="text-white font-semibold text-lg">Janvier 2026</h2>
              <button className="text-purple-400 text-xl">›</button>
            </div>

            {/* Calendar grid */}
            <div className="bg-purple-800/40 rounded-2xl p-4 border border-purple-500/20">
              <div className="grid grid-cols-7 gap-1 text-center text-purple-400 text-xs mb-2">
                {['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'].map(d => (
                  <div key={d}>{d}</div>
                ))}
              </div>
              <div className="grid grid-cols-7 gap-1 text-center">
                {[...Array(31)].map((_, i) => (
                  <div 
                    key={i} 
                    className={`py-2 rounded-lg text-sm ${
                      i === 28 ? 'bg-purple-500 text-white' : 
                      i === 21 ? 'ring-2 ring-purple-400 text-white' :
                      i === 3 ? 'text-yellow-400' :
                      'text-purple-200'
                    }`}
                  >
                    {i + 1}
                  </div>
                ))}
              </div>
            </div>

            {/* VoC Windows à venir */}
            <div className="mt-4 bg-amber-900/20 rounded-2xl p-4 border border-amber-500/20">
              <h3 className="text-amber-400 font-semibold mb-3 flex items-center gap-2">
                <span>⚠️</span> Fenêtres VoC cette semaine
              </h3>
              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-amber-200">Mer 29</span>
                  <span className="text-amber-300/70">09:15 → 14:32</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="text-amber-200">Sam 1</span>
                  <span className="text-amber-300/70">22:45 → 03:12</span>
                </div>
              </div>
            </div>

            {/* Phases */}
            <div className="mt-4 bg-purple-800/40 rounded-2xl p-4 border border-purple-500/20">
              <h3 className="text-yellow-400 font-semibold mb-3">Phases principales</h3>
              <div className="grid grid-cols-2 gap-4">
                <div className="text-center">
                  <p className="text-white font-bold">4 Jan</p>
                  <p className="text-purple-300 text-sm">Pleine Lune</p>
                </div>
                <div className="text-center">
                  <p className="text-white font-bold">11 Jan</p>
                  <p className="text-purple-300 text-sm">Dernier Quartier</p>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Tab: Profil */}
        {activeTab === 'profile' && (
          <div className="px-4 pt-2 pb-4">
            <h1 className="text-2xl font-bold text-white text-center mb-6">Mon Profil</h1>
            
            {/* Avatar */}
            <div className="flex flex-col items-center mb-6">
              <div className="w-20 h-20 rounded-full bg-purple-700 border-2 border-purple-400 flex items-center justify-center mb-2">
                <span className="text-purple-300 text-2xl">♏</span>
              </div>
              <p className="text-white font-semibold">Utilisateur</p>
            </div>

            {/* Thème Natal Card - Expanded */}
            <div className="bg-purple-800/50 rounded-2xl p-5 border border-purple-500/20 mb-4">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-white font-bold text-lg">Mon Thème Natal</h3>
                <button className="text-purple-400 text-sm">Voir complet →</button>
              </div>
              
              {/* Big 3 */}
              <div className="grid grid-cols-3 gap-3 text-center mb-4">
                <div className="bg-purple-900/50 rounded-xl p-3">
                  <div className="w-10 h-10 mx-auto rounded-full bg-yellow-500/20 flex items-center justify-center mb-2">
                    <span className="text-yellow-400 text-xl">☉</span>
                  </div>
                  <p className="text-white font-semibold">Scorpion</p>
                  <p className="text-purple-400 text-xs">Soleil</p>
                </div>
                <div className="bg-purple-900/50 rounded-xl p-3">
                  <div className="w-10 h-10 mx-auto rounded-full bg-purple-500/20 flex items-center justify-center mb-2">
                    <span className="text-purple-300 text-xl">☽</span>
                  </div>
                  <p className="text-white font-semibold">Sagittaire</p>
                  <p className="text-purple-400 text-xs">Lune natale</p>
                </div>
                <div className="bg-purple-900/50 rounded-xl p-3">
                  <div className="w-10 h-10 mx-auto rounded-full bg-pink-500/20 flex items-center justify-center mb-2">
                    <span className="text-pink-400 text-xl">↑</span>
                  </div>
                  <p className="text-white font-semibold">Vierge</p>
                  <p className="text-purple-400 text-xs">Ascendant</p>
                </div>
              </div>

              {/* Planètes supplémentaires */}
              <div className="grid grid-cols-4 gap-2 text-center">
                {[
                  { planet: '☿', sign: 'Sco', name: 'Mercure' },
                  { planet: '♀', sign: 'Sag', name: 'Vénus' },
                  { planet: '♂', sign: 'Sco', name: 'Mars' },
                  { planet: '♃', sign: 'Can', name: 'Jupiter' },
                ].map((p, i) => (
                  <div key={i} className="bg-purple-900/30 rounded-lg p-2">
                    <span className="text-purple-300">{p.planet}</span>
                    <p className="text-white text-xs font-medium">{p.sign}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Birth Info */}
            <div className="bg-purple-800/50 rounded-2xl p-4 border border-purple-500/20 mb-4">
              <h3 className="text-purple-300 font-semibold mb-3">Informations de naissance</h3>
              <div className="space-y-2 text-sm">
                <div className="flex justify-between">
                  <span className="text-purple-400">Date</span>
                  <span className="text-white">1 novembre 1989</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-purple-400">Heure</span>
                  <span className="text-white">13:20</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-purple-400">Lieu</span>
                  <span className="text-white">Manaus, Brésil</span>
                </div>
              </div>
            </div>

            {/* Settings */}
            <div className="bg-purple-800/50 rounded-2xl p-4 border border-purple-500/20">
              <h3 className="text-purple-300 font-semibold mb-3">Paramètres</h3>
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <div>
                    <span className="text-white text-sm">Notifications</span>
                    <p className="text-purple-400 text-xs">VoC & nouveaux cycles</p>
                  </div>
                  <div className="w-12 h-6 bg-purple-500 rounded-full relative">
                    <div className="absolute right-1 top-1 w-4 h-4 bg-white rounded-full"></div>
                  </div>
                </div>
                <div className="flex items-center justify-between">
                  <div>
                    <span className="text-white text-sm">Alertes VoC</span>
                    <p className="text-purple-400 text-xs">15min avant</p>
                  </div>
                  <div className="w-12 h-6 bg-purple-500 rounded-full relative">
                    <div className="absolute right-1 top-1 w-4 h-4 bg-white rounded-full"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Bottom Sheet - Rituel Quotidien */}
      {showBottomSheet && (
        <>
          {/* Backdrop */}
          <div 
            className="absolute inset-0 bg-black/50 transition-opacity"
            onClick={closeSheet}
          ></div>
          
          {/* Sheet */}
          <div 
            className={`absolute bottom-0 left-0 right-0 bg-gradient-to-b from-purple-900 to-purple-950 rounded-t-3xl transition-all duration-300 border-t border-purple-500/30 ${
              sheetHeight === 'full' ? 'h-[90%]' : 'h-[65%]'
            }`}
          >
            {/* Handle */}
            <div className="flex justify-center pt-3 pb-2">
              <div className="w-10 h-1 bg-purple-500/50 rounded-full cursor-pointer" onClick={toggleSheet}></div>
            </div>

            <div className="px-5 overflow-y-auto h-full pb-24">
              {/* Header */}
              <div className="flex items-center gap-3 mb-4">
                <div className="w-12 h-12 rounded-full bg-gradient-to-r from-yellow-100 to-yellow-50 flex items-center justify-center">
                  <span className="text-2xl">🌓</span>
                </div>
                <div>
                  <p className="text-purple-400 text-sm">Aujourd'hui • 29 janvier</p>
                  <h2 className="text-white text-xl font-bold">Lune Gibbeuse Croissante</h2>
                  <p className="text-purple-300 text-sm">en Gémeaux</p>
                </div>
              </div>

              {/* VoC Alert dans le sheet */}
              {vocActive && (
                <div className="mb-4 bg-gradient-to-r from-amber-600/20 to-orange-600/20 rounded-xl p-4 border border-amber-500/30">
                  <div className="flex items-start gap-3">
                    <div className="w-10 h-10 rounded-full bg-amber-500/20 flex items-center justify-center flex-shrink-0">
                      <span className="text-amber-300 text-xl">⏳</span>
                    </div>
                    <div>
                      <p className="text-amber-200 font-semibold">Void of Course en cours</p>
                      <p className="text-amber-300/80 text-sm mt-1">
                        09:15 → 14:32 ({vocEndTime} restant)
                      </p>
                      <p className="text-amber-200/60 text-xs mt-2">
                        La Lune ne forme plus d'aspects majeurs. Période idéale pour la réflexion, 
                        pas pour les nouvelles initiatives.
                      </p>
                    </div>
                  </div>
                </div>
              )}

              {/* Guidance */}
              <div className="bg-purple-800/40 rounded-2xl p-4 mb-4 border border-purple-500/20">
                <h3 className="text-yellow-400 font-semibold mb-2">Guidance du Jour</h3>
                <p className="text-purple-200 text-sm italic mb-3">
                  "Tout continue de mûrir. Tu peux affiner, sans forcer."
                </p>
                <div className="flex flex-wrap gap-2">
                  <span className="px-2 py-1 bg-purple-600/40 rounded text-purple-200 text-xs">Perfectionnement</span>
                  <span className="px-2 py-1 bg-purple-600/40 rounded text-purple-200 text-xs">Patience</span>
                  <span className="px-2 py-1 bg-purple-600/40 rounded text-purple-200 text-xs">Détail</span>
                </div>
              </div>

              {/* Energy bars */}
              <div className="grid grid-cols-2 gap-3 mb-4">
                <div className="bg-purple-800/40 rounded-xl p-3 border border-purple-500/20">
                  <p className="text-purple-400 text-xs mb-1">Énergie Créative</p>
                  <div className="flex items-center gap-2">
                    <div className="flex-1 h-2 bg-purple-900 rounded-full overflow-hidden">
                      <div className="h-full w-full bg-yellow-400 rounded-full"></div>
                    </div>
                    <span className="text-yellow-400 text-sm font-bold">100%</span>
                  </div>
                </div>
                <div className="bg-purple-800/40 rounded-xl p-3 border border-purple-500/20">
                  <p className="text-purple-400 text-xs mb-1">Intuition</p>
                  <div className="flex items-center gap-2">
                    <div className="flex-1 h-2 bg-purple-900 rounded-full overflow-hidden">
                      <div className="h-full w-[90%] bg-purple-400 rounded-full"></div>
                    </div>
                    <span className="text-purple-300 text-sm font-bold">90%</span>
                  </div>
                </div>
              </div>

              {/* Mansion Lunaire */}
              <div className="bg-purple-800/30 rounded-xl p-4 mb-4 border border-purple-500/10">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-indigo-500/20 flex items-center justify-center">
                    <span className="text-indigo-300">✧</span>
                  </div>
                  <div>
                    <p className="text-purple-400 text-xs">Mansion Lunaire #7</p>
                    <p className="text-white font-medium">Al-Dhira (Le Bras)</p>
                    <p className="text-purple-300 text-xs">Favorable aux études et apprentissages</p>
                  </div>
                </div>
              </div>

              {/* Rituels suggérés */}
              <div className="mb-4">
                <h3 className="text-yellow-400 font-semibold mb-3">Rituels suggérés</h3>
                <div className="space-y-2">
                  {[
                    { name: 'Perfectionnement', desc: 'Affinez les détails de vos projets' },
                    { name: 'Gratitude anticipée', desc: 'Remerciez pour ce qui se manifeste' },
                    { name: 'Préparation', desc: 'Préparez la culmination de vos efforts' }
                  ].map((ritual, i) => (
                    <div key={i} className="bg-purple-800/30 rounded-xl p-3 flex items-center justify-between border border-purple-500/10">
                      <div className="flex items-center gap-3">
                        <div className="w-8 h-8 rounded-full bg-purple-700/50 flex items-center justify-center">
                          <span className="text-purple-300 text-sm">✦</span>
                        </div>
                        <div>
                          <span className="text-white text-sm font-medium">{ritual.name}</span>
                          <p className="text-purple-400 text-xs">{ritual.desc}</p>
                        </div>
                      </div>
                      <div className="w-5 h-5 rounded-full border-2 border-purple-500"></div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Journal CTA */}
              <button className="w-full py-3 bg-purple-600/50 rounded-xl text-purple-200 font-medium border border-purple-500/30 flex items-center justify-center gap-2">
                <span>✏️</span>
                <span>Écrire dans mon journal</span>
              </button>
            </div>
          </div>
        </>
      )}

      {/* Tab Bar - 3 tabs */}
      <div className="absolute bottom-0 left-0 right-0 bg-purple-950/95 border-t border-purple-800/50 px-6 py-3 backdrop-blur">
        <div className="flex justify-around">
          <button 
            onClick={() => { setActiveTab('cycle'); closeSheet(); }}
            className={`flex flex-col items-center gap-1 ${activeTab === 'cycle' ? 'text-yellow-400' : 'text-purple-400'}`}
          >
            <span className="text-xl">🌙</span>
            <span className="text-xs font-medium">Mon Cycle</span>
          </button>
          <button 
            onClick={() => { setActiveTab('calendar'); closeSheet(); }}
            className={`flex flex-col items-center gap-1 ${activeTab === 'calendar' ? 'text-yellow-400' : 'text-purple-400'}`}
          >
            <span className="text-xl">📅</span>
            <span className="text-xs font-medium">Calendrier</span>
          </button>
          <button 
            onClick={() => { setActiveTab('profile'); closeSheet(); }}
            className={`flex flex-col items-center gap-1 ${activeTab === 'profile' ? 'text-yellow-400' : 'text-purple-400'}`}
          >
            <span className="text-xl">👤</span>
            <span className="text-xs font-medium">Profil</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default LunationWireframe;
