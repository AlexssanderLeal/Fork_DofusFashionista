# Copyright (C) 2020 The Dofus Fashionista
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from django.utils.translation import ugettext_lazy
from django.utils.translation import ugettext as _


LOCALIZED_CHARACTER_CLASSES = {
    'Eniripsa': ugettext_lazy('Eniripsa'),
    'Iop': ugettext_lazy('Iop'),
    'Xelor': ugettext_lazy('Xelor'),
    'Osamodas': ugettext_lazy('Osamodas'),
    'Feca': ugettext_lazy('Feca'),
    'Sacrier': ugettext_lazy('Sacrier'),
    'Ecaflip': ugettext_lazy('Ecaflip'),
    'Enutrof': ugettext_lazy('Enutrof'),
    'Sram': ugettext_lazy('Sram'),
    'Sadida': ugettext_lazy('Sadida'),
    'Cra': ugettext_lazy('Cra'),
    'Pandawa': ugettext_lazy('Pandawa'),
    'Rogue': ugettext_lazy('Rogue'),
    'Masqueraider': ugettext_lazy('Masqueraider'),
    'Foggernaut': ugettext_lazy('Foggernaut'),
    'Eliotrope': ugettext_lazy('Eliotrope'),
    'Huppermage': ugettext_lazy('Huppermage'),
    'Ouginak': ugettext_lazy('Ouginak'),
}

LOCALIZED_ELEMENTS = {
    'fire': ugettext_lazy('Fire'),
    'earth': ugettext_lazy('Earth'),
    'neut': ugettext_lazy('Neutral'),
    'water': ugettext_lazy('Water'),
    'air': ugettext_lazy('Air'),
}

OTHERS = {
    'project': ugettext_lazy('project'),
    'min_stats_all_but_neut': _('Sum of all % Resists except neutral'),
    'min_stats_all': _('Sum of all % Resists'),
    'min_stats_all_lin': _('Sum of all Linear Resists'),
    'min_stats_all_lin_but_neut': _('Sum of all Linear Resists except neutral'),
}

LOCALIZED_STATS = {
    'HP': ugettext_lazy('HP'),
    'Vitality': ugettext_lazy('Vitality'),
    'Wisdom': ugettext_lazy('Wisdom'),
    'Strength': ugettext_lazy('Strength'),
    'Intelligence': ugettext_lazy('Intelligence'),
    'Chance': ugettext_lazy('Chance'),
    'Agility': ugettext_lazy('Agility'),
    'Power': ugettext_lazy('Power'),
    'AP': ugettext_lazy('AP'),
    'MP': ugettext_lazy('MP'),
    'Range': ugettext_lazy('Range'),
    'Summons': ugettext_lazy('Summons'),
    'Summon': ugettext_lazy('Summon'),
    'Critical Hits': ugettext_lazy('Critical Hits'),
    'Initiative': ugettext_lazy('Initiative'),
    'Prospecting': ugettext_lazy('Prospecting'),
    'Lock': ugettext_lazy('Lock'),
    'Dodge': ugettext_lazy('Dodge'),
    'AP Reduction': ugettext_lazy('AP Reduction'),
    'MP Reduction': ugettext_lazy('MP Reduction'),
    'AP Loss Resist': ugettext_lazy('AP Loss Resist'),
    'MP Loss Resist': ugettext_lazy('MP Loss Resist'),
    'Pushback Resist': ugettext_lazy('Pushback Resist'),
    'Critical Resist': ugettext_lazy('Critical Resist'),
    'Pods': ugettext_lazy('Pods'),
    'Reflects': ugettext_lazy('Reflects'),
    'Trap Damage': ugettext_lazy('Trap Damage'),
    '% Trap Damage': ugettext_lazy('% Trap Damage'),
    'Damage': ugettext_lazy('Damage'),
    'Neutral Damage': ugettext_lazy('Neutral Damage'),
    'Earth Damage': ugettext_lazy('Earth Damage'),
    'Fire Damage': ugettext_lazy('Fire Damage'),
    'Water Damage': ugettext_lazy('Water Damage'),
    'Air Damage': ugettext_lazy('Air Damage'),
    'Critical Damage': ugettext_lazy('Critical Damage'),
    'Pushback Damage': ugettext_lazy('Pushback Damage'),
    'Heals': ugettext_lazy('Heals'),
    'Neutral Resist': ugettext_lazy('Neutral Resist'),
    'Earth Resist': ugettext_lazy('Earth Resist'),
    'Fire Resist': ugettext_lazy('Fire Resist'),
    'Water Resist': ugettext_lazy('Water Resist'),
    'Air Resist': ugettext_lazy('Air Resist'),
    '% Melee Damage': ugettext_lazy('% Melee Damage'),
    '% Ranged Damage': ugettext_lazy('% Ranged Damage'),
    '% Weapon Damage': ugettext_lazy('% Weapon Damage'),
    '% Spell Damage': ugettext_lazy('% Spell Damage'),
    '% Melee Resist': ugettext_lazy('% Melee Resist'),
    '% Ranged Resist': ugettext_lazy('% Ranged Resist'),
}

SPELLS_NAMES = {
    'Perfidious Boomerang': _('Perfidious Boomerang'),
    'Leek Pie': _('Leek Pie'),
    'Moon Hammer': _('Moon Hammer'),
    'Lightning Strike': _('Lightning Strike'),
    'Weapon Skill': _('Weapon Skill'),
    'Magic Arrow': _('Magic Arrow'),
    'Concentration Arrow': _('Concentration Arrow'),
    'Retreat Arrow': _('Retreat Arrow'),
    'Erosive Arrow': _('Erosive Arrow'),
    'Frozen Arrow': _('Frozen Arrow'),
    'Paralyzing Arrow Fire': _('Paralyzing Arrow Fire'),
    'Burning Arrow': _('Burning Arrow'),
    'Repulsive Arrow': _('Repulsive Arrow'),
    'Atonement Arrow': _('Atonement Arrow'),
    'Redemption Arrow': _('Redemption Arrow'),
    "Bat's Eye": _("Bat's Eye"),
    'Crushing Arrow': _('Crushing Arrow'),
    'Critical Shooting': _('Critical Shooting'),
    'Paralyzing Arrow': _('Paralyzing Arrow'),
    'Assailing Arrow': _('Assailing Arrow'),
    'Punitive Arrow': _('Punitive Arrow'),
    'Arrow of Judgement': _('Arrow of Judgement'),
    'Powerful Shooting': _('Powerful Shooting'),
    'Plaguing Arrow': _('Plaguing Arrow'),
    'Slaughtering Arrow': _('Slaughtering Arrow'),
    'Poisoned Arrow': _('Poisoned Arrow'),
    'Tormenting Arrow': _('Tormenting Arrow'),
    'Tyrannical Arrow': _('Tyrannical Arrow'),
    'Destructive Arrow': _('Destructive Arrow'),
    'Barricade Shot': _('Barricade Shot'),
    'Absorptive Arrow': _('Absorptive Arrow'),
    'Devouring Arrow': _('Devouring Arrow'),
    'Slow Down Arrow': _('Slow Down Arrow'),
    'Striking Arrow': _('Striking Arrow'),
    'Explosive Arrow': _('Explosive Arrow'),
    'Fulminating Arrow': _('Fulminating Arrow'),
    'Bow Skill': _('Bow Skill'),
    'Sentinel': _('Sentinel'),
    'Heads or Tails 1': _('Heads or Tails 1'),
    'Heads or Tails 2': _('Heads or Tails 2'),
    'Bluff': _('Bluff'),
    'Nerve': _('Nerve'),
    'Topkaj': _('Topkaj'),
    'Yowling': _('Yowling'),
    'All or Nothing': _('All or Nothing'),
    'Peril': _('Peril'),
    'Rough Tongue': _('Rough Tongue'),
    'Lapping Up': _('Lapping Up'),
    'Wheel of Fortune': _('Wheel of Fortune'),
    'Feline Spirit': _('Feline Spirit'),
    'Pawpads': _('Pawpads'),
    'Reflex': _('Reflex'),
    'Bravado': _('Bravado'),
    'Playful Claw': _('Playful Claw'),
    'Misadventure': _('Misadventure'),
    'Felintion': _('Felintion'),
    'Kraps': _('Kraps'),
    'Claw of Ceangal': _('Claw of Ceangal'),
    'Misfortune': _('Misfortune'),
    'Rekop': _('Rekop'),
    'Trickery': _('Trickery'),
    'Fate of Ecaflip': _('Fate of Ecaflip'),
    "Ecaflip's Audacity": _("Ecaflip's Audacity"),
    'Alternative Word': _('Alternative Word'),
    'Striking Word': _('Striking Word'),
    'Wounding Word': _('Wounding Word'),
    'Slighting Word': _('Slighting Word'),
    'Forbidden Word': _('Forbidden Word'),
    'Taboo Word': _('Taboo Word'),
    'Seductive Word': _('Seductive Word'),
    'Self-Sacrificing Word': _('Self-Sacrificing Word'),
    'Brutal Word': _('Brutal Word'),
    'Pernicious Word': _('Pernicious Word'),
    'Defensive Word': _('Defensive Word'),
    'Selective Word': _('Selective Word'),
    'Impartial Word': _('Impartial Word'),
    'Blaring Word': _('Blaring Word'),
    'Resounding Word': _('Resounding Word'),
    'Agonising Word': _('Agonising Word'),
    'Turbulent Word': _('Turbulent Word'),
    'Mischievous Word': _('Mischievous Word'),
    'Puzzling Word': _('Puzzling Word'),
    'Furious Word': _('Furious Word'),
    'Whirling Word 1': _('Whirling Word 1'),
    'Whirling Word 2': _('Whirling Word 2'),
    'Thunderous Word': _('Thunderous Word'),
    'Overwhelming Word': _('Overwhelming Word'),
    'Coins Throwing': _('Coins Throwing'),
    'Hard Cash': _('Hard Cash'),
    'Shovel Throwing': _('Shovel Throwing'),
    'Spade Throw': _('Spade Throw'),
    'Ghostly Shovel': _('Ghostly Shovel'),
    'Ghostly Spade': _('Ghostly Spade'),
    'Mound': _('Mound'),
    'Peat Bog': _('Peat Bog'),
    'Prime of Life': _('Prime of Life'),
    'Obsolescence': _('Obsolescence'),
    'Greed': _('Greed'),
    'Shovel Kiss': _('Shovel Kiss'),
    'Spade Kiss': _('Spade Kiss'),
    'Loafylactic': _('Loafylactic'),
    'Fortune': _('Fortune'),
    'Opportuneness': _('Opportuneness'),
    'Shovel of Judgment': _('Shovel of Judgment'),
    'Spade of Judgment': _('Spade of Judgment'),
    'Slaughtering Shovel': _('Slaughtering Shovel'),
    'Carnivore Spade': _('Carnivore Spade'),
    'Unsummoning': _('Unsummoning'),
    'Correction': _('Correction'),
    'Natural Attack': _('Natural Attack'),
    'Natural Attraction': _('Natural Attraction'),
    'Blindness': _('Blindness'),
    'Dazzling': _('Dazzling'),
    'Typhoon': _('Typhoon'),
    'Gust': _('Gust'),
    'Bubble': _('Bubble'),
    'Swelling': _('Swelling'),
    'Aggressive Glyph': _('Aggressive Glyph'),
    'Fulminating Glyph': _('Fulminating Glyph'),
    'Lethargy': _('Lethargy'),
    'Lifelessness': _('Lifelessness'),
    'Cloudy Attack': _('Cloudy Attack'),
    'Stormy Attack': _('Stormy Attack'),
    'Bastion': _('Bastion'),
    'Backlash': _('Backlash'),
    'Tetany': _('Tetany'),
    'Repulsion Glyph': _('Repulsion Glyph'),
    'Barrier': _('Barrier'),
    'Blinding Glyph': _('Blinding Glyph'),
    'Protective Glyph': _('Protective Glyph'),
    'Shiver': _('Shiver'),
    'Tension': _('Tension'),
    'Paralyzing Glyph': _('Paralyzing Glyph'),
    'Roaming Glyph': _('Roaming Glyph'),
    'Reinforced Protection': _('Reinforced Protection'),
    'Burning Glyph': _('Burning Glyph'),
    'Perception Glyph': _('Perception Glyph'),
    'Anchor': _('Anchor'),
    'Mooring': _('Mooring'),
    'Pilfer': _('Pilfer'),
    'Scuttle': _('Scuttle'),
    'Torrent': _('Torrent'),
    'Harmattan': _('Harmattan'),
    'Scaphander': _('Scaphander'),
    'Backwash': _('Backwash'),
    'Torpedo': _('Torpedo'),
    'Tide': _('Tide'),
    'Corrosion': _('Corrosion'),
    'Vapour': _('Vapour'),
    'Valve': _('Valve'),
    'Periscope 1': _('Periscope 1'),
    'Periscope 2': _('Periscope 2'),
    'First Aid': _('First Aid'),
    'Rescue': _('Rescue'),
    'Surge': _('Surge'),
    'Short-Circuit': _('Short-Circuit'),
    'Ambush': _('Ambush'),
    'Froth': _('Froth'),
    'Nautilus': _('Nautilus'),
    'Trident': _('Trident'),
    'Seizing': _('Seizing'),
    'Intimidation': _('Intimidation'),
    'Pressure': _('Pressure'),
    'Pounding': _('Pounding'),
    'Outpouring': _('Outpouring'),
    'Threat': _('Threat'),
    'Divine Sword': _('Divine Sword'),
    'Cleaver': _('Cleaver'),
    'Destructive Sword': _('Destructive Sword'),
    'Destructive Ring': _('Destructive Ring'),
    'Concentration': _('Concentration'),
    'Accumulation': _('Accumulation'),
    'Cut': _('Cut'),
    'Fracture': _('Fracture'),
    'Sword of Judgement': _('Sword of Judgement'),
    'Condemnation': _('Condemnation'),
    'Power': _('Power'),
    'Strengthstorm': _('Strengthstorm'),
    'Tumult': _('Tumult'),
    'Celestial Sword': _('Celestial Sword'),
    'Zenith': _('Zenith'),
    'Endurance': _('Endurance'),
    'Sword of Iop': _('Sword of Iop'),
    'Pygmachia': _('Pygmachia'),
    'Sword of Fate': _('Sword of Fate'),
    'Sentence': _('Sentence'),
    "Iop's Wrath": _("Iop's Wrath"),
    'Fit of Rage': _('Fit of Rage'),
    'Picada': _('Picada'),
    'Agular': _('Agular'),
    'Martelo': _('Martelo'),
    'Parafuso': _('Parafuso'),
    'Reinforcement': _('Reinforcement'),
    'Retention': _('Retention'),
    'Estrelia': _('Estrelia'),
    'Furia': _('Furia'),
    'Cavalcade': _('Cavalcade'),
    'Distance': _('Distance'),
    'Atabak': _('Atabak'),
    'Ginga': _('Ginga'),
    'Neurosis': _('Neurosis'),
    'Capering': _('Capering'),
    'Bocciara': _('Bocciara'),
    'Decoy': _('Decoy'),
    'Catalepsy': _('Catalepsy'),
    'Apostasy': _('Apostasy'),
    'Brincaderia': _('Brincaderia'),
    'Apathy': _('Apathy'),
    'Ponteira': _('Ponteira'),
    'Boliche': _('Boliche'),
    'Inferno': _('Inferno'),
    'Canine': _('Canine'),
    'Repulsive Fang': _('Repulsive Fang'),
    'Dragonic': _('Dragonic'),
    'Aquatic Wave': _('Aquatic Wave'),
    'Fossil': _('Fossil'),
    'Sedimentation': _('Sedimentation'),
    'Takeoff': _('Takeoff'),
    'Whip': _('Whip'),
    'Duster': _('Duster'),
    'Plucking': _('Plucking'),
    "Dragon's Breath": _("Dragon's Breath"),
    'Crackler Punch': _('Crackler Punch'),
    'Constriction': _('Constriction'),
    'Geyser': _('Geyser'),
    'Whirlwind': _('Whirlwind'),
    'Blazing Fist': _('Blazing Fist'),
    'Burning Circle': _('Burning Circle'),
    'Debauchery': _('Debauchery'),
    'Hangover': _('Hangover'),
    'Alcoholic Breath': _('Alcoholic Breath'),
    'Numbness': _('Numbness'),
    'Schnaps': _('Schnaps'),
    'Liqueur': _('Liqueur'),
    'Propulsion': _('Propulsion'),
    'Eviction': _('Eviction'),
    'Nausea': _('Nausea'),
    'Tipple': _('Tipple'),
    'Distillation': _('Distillation'),
    'Melancholy': _('Melancholy'),
    'Hooch': _('Hooch'),
    "Zatoishwan's Wrath": _("Zatoishwan's Wrath"),
    'Explosive Flask': _('Explosive Flask'),
    'Absinthe': _('Absinthe'),
    'Pandatak': _('Pandatak'),
    'Filthipint': _('Filthipint'),
    'Explobomb': _('Explobomb'),
    'Extraction': _('Extraction'),
    'Obliteration': _('Obliteration'),
    'Musket': _('Musket'),
    'Grenado': _('Grenado'),
    'Boomerang Daggers': _('Boomerang Daggers'),
    'Cadence': _('Cadence'),
    'Deception': _('Deception'),
    'Stolen Goods': _('Stolen Goods'),
    'Water Bomb': _('Water Bomb'),
    'Pulsar': _('Pulsar'),
    'Gluing Explobomb': _('Gluing Explobomb'),
    'Arquebus': _('Arquebus'),
    'Carbine': _('Carbine'),
    'Machine Gun': _('Machine Gun'),
    'Last Breath': _('Last Breath'),
    'Seismobomb': _('Seismobomb'),
    'Blunderbuss': _('Blunderbuss'),
    'Weigh Down': _('Weigh Down'),
    'Absorption': _('Absorption'),
    'Slaughter': _('Slaughter'),
    'Fury': _('Fury'),
    'Carnage': _('Carnage'),
    'Stase': _('Stase'),
    'Dissolution': _('Dissolution'),
    'Motivating Pain': _('Motivating Pain'),
    'Cauterisation': _('Cauterisation'),
    'Assault': _('Assault'),
    'Aversion': _('Aversion'),
    'Mutilation': _('Mutilation'),
    'Light Speed': _('Light Speed'),
    'Condensation': _('Condensation'),
    'Nervousness': _('Nervousness'),
    'Clobbering': _('Clobbering'),
    'Projection': _('Projection'),
    'Hostility': _('Hostility'),
    'Torture': _('Torture'),
    'Desolation': _('Desolation'),
    'Influx': _('Influx'),
    'Ravages': _('Ravages'),
    'Decimation': _('Decimation'),
    'Gash': _('Gash'),
    'Blood Bath': _('Blood Bath'),
    'Ritual Bloodletting': _('Ritual Bloodletting'),
    'Bramble': _('Bramble'),
    'Poisoned Undergrowth': _('Poisoned Undergrowth'),
    'Paralysing Poison': _('Paralysing Poison'),
    'Tear': _('Tear'),
    'Rise of Sap': _('Rise of Sap'),
    'Soothing Bramble': _('Soothing Bramble'),
    'Earthquake': _('Earthquake'),
    'Shake': _('Shake'),
    'Natural Gift': _('Natural Gift'),
    'Inoculation': _('Inoculation'),
    'Manifold Bramble': _('Manifold Bramble'),
    'Force of Nature': _('Force of Nature'),
    'Dolly Sacrifice': _('Dolly Sacrifice'),
    'Bane': _('Bane'),
    'Aggressive Bramble': _('Aggressive Bramble'),
    'Plaguing Bramble': _('Plaguing Bramble'),
    'Wild Grass': _('Wild Grass'),
    'Contagion': _('Contagion'),
    'Bush Fire': _('Bush Fire'),
    'Voodoo Curse': _('Voodoo Curse'),
    'Paralysing Bramble': _('Paralysing Bramble'),
    'Tricky Trap': _('Tricky Trap'),
    'Deviousness': _('Deviousness'),
    'Pitfall': _('Pitfall'),
    'Insidious Poison': _('Insidious Poison'),
    'Toxines': _('Toxines'),
    'Mistake': _('Mistake'),
    'Raiding': _('Raiding'),
    'Tricky Blow': _('Tricky Blow'),
    'Cut-Throat': _('Cut-Throat'),
    'Miry Trap': _('Miry Trap'),
    'Larceny': _('Larceny'),
    'Mass Trap': _('Mass Trap'),
    'Trapster': _('Trapster'),
    'Cruelty': _('Cruelty'),
    'Ambush': _('Ambush'),
    'Poisoned Trap': _('Poisoned Trap'),
    'Toxic Injection': _('Toxic Injection'),
    'Chakra Concentration': _('Chakra Concentration'),
    'Fragmentation Trap': _('Fragmentation Trap'),
    'Insidious Trap': _('Insidious Trap'),
    'Epidemic': _('Epidemic'),
    'Repelling Trap': _('Repelling Trap'),
    'Con': _('Con'),
    'Jinx': _('Jinx'),
    'Calamity': _('Calamity'),
    'Furrow': _('Furrow'),
    'Perquisition': _('Perquisition'),
    'Lethal Attack': _('Lethal Attack'),
    'Malevolent Trap': _('Malevolent Trap'),
    'Lethal Trap': _('Lethal Trap'),
    'Perfidy': _('Perfidy'),
    'Slow Down': _('Slow Down'),
    'Souvenir': _('Souvenir'),
    'Hand': _('Hand'),
    'Cog': _('Cog'),
    'Shriveling': _('Shriveling'),
    'Drying Up': _('Drying Up'),
    "Xelor's Punch": _("Xelor's Punch"),
    'Gear': _('Gear'),
    'Frostbite': _('Frostbite'),
    'Disruption': _('Disruption'),
    "Xelor's Sandglass": _("Xelor's Sandglass"),
    'Temporal Distortion': _('Temporal Distortion'),
    'Time Theft': _('Time Theft'),
    'Petrification': _('Petrification'),
    'Temporal Dust': _('Temporal Dust'),
    'Temporal Suspension': _('Temporal Suspension'),
    'Loss of Motivation': _('Loss of Motivation'),
    'Pendulum': _('Pendulum'),
    'Clock': _('Clock'),
    'Water Clock': _('Water Clock'),
    'Dark Ray': _('Dark Ray'),
    'Shadowy Beam': _('Shadowy Beam'),
    'Knell': _('Knell'),
    'Affliction': _('Affliction'),
    'Tribulation': _('Tribulation'),
    'Insult': _('Insult'),
    'Contempt': _('Contempt'),
    'Shock': _('Shock'),
    'Convulsion': _('Convulsion'),
    'Wakfu Ray': _('Wakfu Ray'),
    'Lazybeam': _('Lazybeam'),
    'Offence': _('Offence'),
    'Affront': _('Affront'),
    'Therapy': _('Therapy'),
    'Sinecure': _('Sinecure'),
    'Bullying': _('Bullying'),
    'Correction': _('Correction'),
    'Lightning Fist': _('Lightning Fist'),
    'Snub': _('Snub'),
    'Audacious': _('Audacious'),
    'Composure': _('Composure'),
    'Focus': _('Focus'),
    'Parasite': _('Parasite'),
    'Virus': _('Virus'),
    'Ridicule': _('Ridicule'),
    'Persiflage': _('Persiflage'),
    'Ether': _('Ether'),
    'Stinger': _('Stinger'),
    'Telluric Wave': _('Telluric Wave'),
    'Celestial Wave': _('Celestial Wave'),
    'Flamethrower': _('Flamethrower'),
    'Cataract': _('Cataract'),
    'Stalagmite': _('Stalagmite'),
    'Ember': _('Ember'),
    'Elemental Drain': _('Elemental Drain'),
    'Morph': _('Morph'),
    'Storm': _('Storm'),
    'Tectonic Breach': _('Tectonic Breach'),
    'Astral Blade': _('Astral Blade'),
    'Telluric Blade': _('Telluric Blade'),
    'Burning Stroke': _('Burning Stroke'),
    'Volcano': _('Volcano'),
    'Glacier': _('Glacier'),
    'Stalactite': _('Stalactite'),
    'Journey': _('Journey'),
    'Deflagration': _('Deflagration'),
    'Flood': _('Flood'),
    'Contribution': _('Contribution'),
    'Icy Shards': _('Icy Shards'),
    'Sun Lance': _('Sun Lance'),
    'Transfixing Gust': _('Transfixing Gust'),
    'Hurricane': _('Hurricane'),
    'Striking Meteor': _('Striking Meteor'),
    'Comet': _('Comet'),
    'Watchdog': _('Watchdog'),
    'Jaw': _('Jaw'),
    'Ulna': _('Ulna'),
    'Calcaneus': _('Calcaneus'),
    'Carcass': _('Carcass'),
    'Stripping': _('Stripping'),
    'Cutting Down': _('Cutting Down'),
    'Woof': _('Woof'),
    'Mastiff': _('Mastiff'),
    'Muzzle': _('Muzzle'),
    'Tibia': _('Tibia'),
    'Humerous': _('Humerous'),
    'Tracking': _('Tracking'),
    'Hunt': _('Hunt'),
    'Bloodhound': _('Bloodhound'),
    'Beaten': _('Beaten'),
    'R-Canine': _('R-Canine'),
    'Carrion': _('Carrion'),
    'Radius': _('Radius'),
    'Marrow Bone': _('Marrow Bone'),
    'Vertebra': _('Vertebra'),
    'Cerberus': _('Cerberus'),
    'Amarok': _('Amarok'),
    'Tetanisation': _('Tetanisation'),
    'Carving Up': _('Carving Up'),
}

SPELLS_EFFECTS = {
    '25% chance of': _('25% chance of'),
    'Not charged': _('Not charged'),
    'Not Charged': _('Not Charged'),
    'Charged once': _('Charged once'),
    'Charged twice': _('Charged twice'),
    'If the target is pushed': _('If the target is pushed'),
    'If the target suffers pushback damage': _('If the target suffers pushback damage'),
    'Regular shot': _('Regular shot'),
    'After postponing once': _('After postponing once'),
    'After postponing twice': _('After postponing twice'),
    'Enemies': _('Enemies'),
    'Allies': _('Allies'),
    'Enemies (imediately)': _('Enemies (imediately)'),
    'Enemies (next turn)': _('Enemies (next turn)'),
    'Allies (imediately)': _('Allies (imediately)'),
    'Allies (next turn)': _('Allies (next turn)'),
    'If the target has more than 50% HP': _('If the target has more than 50% HP'),
    'If the target has less than 50% HP': _('If the target has less than 50% HP'),
    'In one turn': _('In one turn'),
    'In two turns': _('In two turns'),
    'In three turns': _('In three turns'),
    'If the target is pushed': _('If the target is pushed'),
    'Enemy or around ally': _('Enemy or around ally'),
    'Ally or around enemy': _('Ally or around enemy'),
    'Non-summons': _('Non-summons'),
    'Summons': _('Summons'),
    'Hit': _('Hit'),
    'Pushback Poison': _('Pushback Poison'),
    'Other': _('Other'),
    'Charged': _('Charged'),
    'Tofu': _('Tofu'),
    'Gobball': _('Gobball'),
    'Toad': _('Toad'),
    'Wyrmling (enemies)': _('Wyrmling (enemies)'),
    'Wyrmling (allies)': _('Wyrmling (allies)'),
    'No Tofus': _('No Tofus'),
    'One Tofu': _('One Tofu'),
    'Two Tofus': _('Two Tofus'),
    'Three Tofus': _('Three Tofus'),
    'Four Tofus': _('Four Tofus'),
    'Five Tofus': _('Five Tofus'),
    'If an Explobomb is present': _('If an Explobomb is present'),
    'If a Grenado is present': _('If a Grenado is present'),
    'If a Waterbomb is present': _('If a Waterbomb is present'),
    'If a Seismobomb is present': _('If a Seismobomb is present'),
    'Allies/Summons': _('Allies/Summons'),
    'If the target loses MP': _('If the target loses MP'),
    'If the target loses AP': _('If the target loses AP'),
    'At the center': _('At the center'),
    'One tile away from the center': _('One tile away from the center'),
    'Two tiles away from the center': _('Two tiles away from the center'),
    'Three tiles away from the center': _('Three tiles away from the center'),
    'Directly': _('Directly'),
    'Through a portal': _('Through a portal'),
    'Target in air state': _('Target in air state'),
    'Target in fire state': _('Target in fire state'),
    'Target in water state': _('Target in water state'),
    'Target in earth state': _('Target in earth state'),
    'If the target is Prey': _('If the target is Prey'),
    'After hitting a Prey': _('After hitting a Prey once'),
    'After hitting a Prey': _('After hitting a Prey twice'),
    'After hitting a Prey': _('After hitting a Prey 3x'),
    'After hitting a Prey': _('After hitting a Prey 4x'),
    'After hitting a Prey': _('After hitting a Prey 5x'),
    
}

LOCALIZED_WEAPON_TYPES = {
    'Hammer': ugettext_lazy('Hammer'),
    'Axe': ugettext_lazy('Axe'),
    'Shovel': ugettext_lazy('Shovel'),
    'Staff': ugettext_lazy('Staff'),
    'Sword': ugettext_lazy('Sword'),
    'Dagger': ugettext_lazy('Dagger'),
    'Bow': ugettext_lazy('Bow'),
    'Wand': ugettext_lazy('Wand'),
    'Pickaxe': ugettext_lazy('Pickaxe'),
    'Scythe': ugettext_lazy('Scythe'),
}
"""
OTHER_STRINGS = {
    'shield_violation': _("Can't equip a two handed weapon and a shield.")
}
"""